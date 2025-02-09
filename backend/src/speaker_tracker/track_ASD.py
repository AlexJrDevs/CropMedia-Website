import sys
import time
import os
import tqdm
import torch
import glob
import subprocess
import warnings
import cv2
import pickle
import numpy as np
import math
import python_speech_features
from pathlib import Path

from scipy import signal
from shutil import rmtree
from scipy.io import wavfile
from scipy.interpolate import interp1d

from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector

from .model.faceDetector.s3fd import S3FD
from .ASD import ASD

warnings.filterwarnings("ignore")

class LightASD:

    def __init__(self, 
              video_path, # Path: video name
              fine_tuned_model, # Bool: To turn on / off fine tuned model
              n_data_loader_thread=10, # Int: Number of workers For Subprocess To Use
              facedet_scale=0.25, # Float: Scale factor for face detection, the frames will be scale to 0.25 orig
              min_track=10, # Int: Number of min frames for each shot
              num_failed_det=10, # Int: Number of missed detections allowed before tracking is stopped
              min_face_size=1, # Int: Minimum face size in pixels
              crop_scale=0.40, # Float: Scale bounding box
              start=0, # Int: The start time of the video in seconds
              duration=0, # Int: The duration of the video, when set as 0, will extract the whole video
            ):
        
        self.video_path = video_path

        self.n_data_loader_thread = n_data_loader_thread
        self.facedet_scale = facedet_scale
        self.min_track = min_track
        self.num_failed_det = num_failed_det
        self.min_face_size = min_face_size
        self.crop_scale = crop_scale
        self.start = start
        self.duration = duration

        # Define the project root directory
        PROJECT_ROOT = Path(__file__).resolve().parent  # Adjust based on your project structure
        print(f"Project Root: {PROJECT_ROOT}")

        # Define paths relative to the project root
        weight_dir = PROJECT_ROOT / "weight"
        self.save_path = PROJECT_ROOT / "save_location"

        # Ensure directories exist
        weight_dir.mkdir(parents=True, exist_ok=True)
        self.save_path.mkdir(parents=True, exist_ok=True)

        # Define file paths
        if fine_tuned_model:
            self.pretrain_model = weight_dir / "finetuning_TalkSet.model"
        else:
            self.pretrain_model = weight_dir / "pretrain_AVA_CVPR.model"

        self.pyavi_path = os.path.join(self.save_path, 'pyavi')
        self.pyframes_path = os.path.join(self.save_path, 'pyframes')
        self.pywork_path = os.path.join(self.save_path, 'pywork')
        self.pycrop_path = os.path.join(self.save_path, 'pycrop')


        # Create directories
        os.makedirs(self.pyavi_path, exist_ok=True)
        os.makedirs(self.pyframes_path, exist_ok=True)
        os.makedirs(self.pywork_path, exist_ok=True)
        os.makedirs(self.pycrop_path, exist_ok=True)


    def scene_detect(self):
        video_manager = VideoManager([self.video_path])
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)
        scene_manager.add_detector(ContentDetector())
        base_timecode = video_manager.get_base_timecode()
        video_manager.set_downscale_factor()
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        scene_list = scene_manager.get_scene_list(base_timecode)
        save_path = os.path.join(self.pywork_path, 'scene.pckl')
        if not scene_list:
            scene_list = [(video_manager.get_base_timecode(), video_manager.get_current_timecode())]
        with open(save_path, 'wb') as fil:
            pickle.dump(scene_list, fil)

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Scenes detected: {len(scene_list)}")
        return scene_list

    def inference_video(self):
        det = S3FD(device='cuda')
        flist = glob.glob(os.path.join(self.pyframes_path, '*.jpg'))
        flist.sort()
        dets = []
        for fidx, fname in enumerate(flist):
            image = cv2.imread(fname)
            image_numpy = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            bboxes = det.detect_faces(image_numpy, conf_th=0.9, scales=[self.facedet_scale])
            dets.append([])

            # Dynamic progress print (updates the same line)
            print(f"Processing Frame {fidx + 1}/{len(flist)}...", end="\r")
            for bbox in bboxes:
                dets[-1].append({'frame': fidx, 'bbox': (bbox[:-1]).tolist(), 'conf': bbox[-1]})

        # Print a newline after the loop to ensure the final output is clean
        print()

        save_path = os.path.join(self.pywork_path, 'faces.pckl')
        with open(save_path, 'wb') as fil:
            pickle.dump(dets, fil)
        return dets

    def track_shot(self, scene_faces):
        iou_thres = 0.5
        tracks = []
        while True:
            track = []
            for frame_faces in scene_faces:
                for face in frame_faces:
                    if not track:
                        track.append(face)
                        frame_faces.remove(face)
                    elif face['frame'] - track[-1]['frame'] <= self.num_failed_det:
                        iou = self.bb_intersection_over_union(face['bbox'], track[-1]['bbox'])
                        if iou > iou_thres:
                            track.append(face)
                            frame_faces.remove(face)
                            continue
                    else:
                        break
            if not track:
                break
            elif len(track) > self.min_track:
                frame_num = np.array([f['frame'] for f in track])
                bboxes = np.array([np.array(f['bbox']) for f in track])
                frame_i = np.arange(frame_num[0], frame_num[-1] + 1)
                bboxes_i = []
                for ij in range(0, 4):
                    interp_fn = interp1d(frame_num, bboxes[:, ij])
                    bboxes_i.append(interp_fn(frame_i))
                bboxes_i = np.stack(bboxes_i, axis=1)
                if max(np.mean(bboxes_i[:, 2] - bboxes_i[:, 0]), np.mean(bboxes_i[:, 3] - bboxes_i[:, 1])) > self.min_face_size:
                    tracks.append({'frame': frame_i, 'bbox': bboxes_i})
        return tracks

    def bb_intersection_over_union(self, box_a, box_b, eval_col=False):
        x_a = max(box_a[0], box_b[0])
        y_a = max(box_a[1], box_b[1])
        x_b = min(box_a[2], box_b[2])
        y_b = min(box_a[3], box_b[3])
        inter_area = max(0, x_b - x_a) * max(0, y_b - y_a)
        box_a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
        box_b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
        if eval_col:
            iou = inter_area / float(box_a_area)
        else:
            iou = inter_area / float(box_a_area + box_b_area - inter_area)
        return iou

    def crop_video(self, track, crop_file):
        flist = glob.glob(os.path.join(self.pyframes_path, '*.jpg'))
        flist.sort()
        v_out = cv2.VideoWriter(crop_file + 't.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (224, 224))
        dets = {'x': [], 'y': [], 's': []}
        for det in track['bbox']:
            dets['s'].append(max((det[3] - det[1]), (det[2] - det[0])) / 2)
            dets['y'].append((det[1] + det[3]) / 2)
            dets['x'].append((det[0] + det[2]) / 2)
        dets['s'] = signal.medfilt(dets['s'], kernel_size=13)
        dets['x'] = signal.medfilt(dets['x'], kernel_size=13)
        dets['y'] = signal.medfilt(dets['y'], kernel_size=13)
        for fidx, frame in enumerate(track['frame']):
            cs = self.crop_scale
            bs = dets['s'][fidx]
            bsi = int(bs * (1 + 2 * cs))
            image = cv2.imread(flist[frame])
            frame = np.pad(image, ((bsi, bsi), (bsi, bsi), (0, 0)), 'constant', constant_values=(110, 110))
            my = dets['y'][fidx] + bsi
            mx = dets['x'][fidx] + bsi
            face = frame[int(my - bs):int(my + bs * (1 + 2 * cs)), int(mx - bs * (1 + cs)):int(mx + bs * (1 + cs))]
            v_out.write(cv2.resize(face, (224, 224)))
        audio_tmp = crop_file + '.wav'
        audio_start = (track['frame'][0]) / 25
        audio_end = (track['frame'][-1] + 1) / 25
        v_out.release()
        command = ("ffmpeg -y -i %s -async 1 -ac 1 -vn -acodec pcm_s16le -ar 16000 -threads %d -ss %.3f -to %.3f %s -loglevel panic" %
                (self.video_path, self.n_data_loader_thread, audio_start, audio_end, audio_tmp))
        self.run_command(command)
        _, audio = wavfile.read(audio_tmp)
        command = ("ffmpeg -y -i %st.avi -i %s -threads %d -c:v copy -c:a copy %s.avi -loglevel panic" %
                (crop_file, audio_tmp, self.n_data_loader_thread, crop_file))
        self.run_command(command)
        os.remove(crop_file + 't.avi')
        return {'track': track, 'proc_track': dets}

    def evaluate_network(self, files):
        s = ASD()
        s.loadParameters(self.pretrain_model)
        s.eval()
        all_scores = []
        duration_set = {1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6}
        for file in tqdm.tqdm(files, total=len(files)):
            file_name = os.path.splitext(os.path.basename(file))[0]
            _, audio = wavfile.read(os.path.join(self.pycrop_path, file_name + '.wav'))
            audio_feature = python_speech_features.mfcc(audio, 16000, numcep=13, winlen=0.025, winstep=0.010)
            video = cv2.VideoCapture(os.path.join(self.pycrop_path, file_name + '.avi'))
            video_feature = []
            while video.isOpened():
                ret, frames = video.read()
                if ret:
                    face = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
                    face = cv2.resize(face, (224, 224))
                    face = face[int(112 - (112 / 2)):int(112 + (112 / 2)), int(112 - (112 / 2)):int(112 + (112 / 2))]
                    video_feature.append(face)
                else:
                    break
            video.release()
            video_feature = np.array(video_feature)
            length = min((audio_feature.shape[0] - audio_feature.shape[0] % 4) / 100, video_feature.shape[0])
            audio_feature = audio_feature[:int(round(length * 100)), :]
            video_feature = video_feature[:int(round(length * 25)), :, :]
            all_score = []
            for duration in duration_set:
                batch_size = int(math.ceil(length / duration))
                scores = []
                with torch.no_grad():
                    for i in range(batch_size):
                        input_a = torch.FloatTensor(audio_feature[i * duration * 100:(i + 1) * duration * 100, :]).unsqueeze(0).cuda()
                        input_v = torch.FloatTensor(video_feature[i * duration * 25: (i + 1) * duration * 25, :, :]).unsqueeze(0).cuda()
                        embed_a = s.model.forward_audio_frontend(input_a)
                        embed_v = s.model.forward_visual_frontend(input_v)
                        out = s.model.forward_audio_visual_backend(embed_a, embed_v)
                        score = s.lossAV.forward(out, labels=None)
                        scores.extend(score)
                all_score.append(scores)
            all_score = np.round((np.mean(np.array(all_score), axis=0)), 1).astype(float)
            all_scores.append(all_score)
        return all_scores
    

    def run_command(self, command):
        """Helper function to run a command and capture output/errors."""
        process = subprocess.Popen(
			command, 
			shell=True, 
			stdout=None, # Use subprocess.PIPE if you want to see a timer
			stderr=subprocess.PIPE
		)
        stderr = process.communicate()[1] # Remove the [1] and add stdout next to stderr to capture live output
        
        if process.returncode != 0:
            print(f"Command Error: {stderr.decode('utf-8')}")


    def run(self):
        # Extract video
        video_file_path = os.path.join(self.pyavi_path, 'video.avi')
        
        if self.duration == 0:
            command = ("ffmpeg -y -i %s -qscale:v 2 -threads %d -async 1 -r 25 %s " %
                    (self.video_path, self.n_data_loader_thread, video_file_path))
        else:
            command = ("ffmpeg -y -i %s -qscale:v 2 -threads %d -ss %.3f -to %.3f -async 1 -r 25 %s -loglevel panic" %
                    (self.video_path, self.n_data_loader_thread, self.start, self.start + self.duration, video_file_path))
        print("Extracting Video")
        self.run_command(command)

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Video extracted.")

        # Extract the video frames
        command = ("ffmpeg -y -i %s -qscale:v 2 -threads %d -f image2 %s -loglevel panic" %
                (video_file_path, self.n_data_loader_thread, os.path.join(self.pyframes_path, '%06d.jpg')))
        print("Extrating Video Frames")
        self.run_command(command)

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Frames extracted.")

        # Scene detection for the video frames
        scene = self.scene_detect()

        # Face detection for the video frames
        faces = self.inference_video()

        # Face tracking
        all_tracks = []
        for idx, shot in enumerate(scene):
            if shot[1].frame_num - shot[0].frame_num >= self.min_track:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Processing shot {idx + 1}/{len(scene)}...")
                all_tracks.extend(self.track_shot(faces[shot[0].frame_num:shot[1].frame_num]))

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Face tracking completed. Detected {len(all_tracks)} tracks.")

        # Face clips cropping
        vid_tracks = []
        for ii, track in tqdm.tqdm(enumerate(all_tracks), total=len(all_tracks)):
            vid_tracks.append(self.crop_video(track, os.path.join(self.pycrop_path, '%05d' % ii)))
        save_path = os.path.join(self.pywork_path, 'tracks.pckl')
        with open(save_path, 'wb') as fil:
            pickle.dump(vid_tracks, fil)

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Face cropping completed. Saved in {self.pycrop_path}.")

        # Active Speaker Detection
        files = glob.glob(os.path.join(self.pycrop_path, "*.avi"))
        files.sort()
        scores = self.evaluate_network(files)
        save_path = os.path.join(self.pywork_path, 'scores.pckl')
        with open(save_path, 'wb') as fil:
            pickle.dump(scores, fil)

        # Debugging print
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Scores extracted and saved in {self.pywork_path}.")



        # Return face tracking information
        return vid_tracks, scores, self.pyframes_path


    def clean_up(self):
        # Cleans Up Files
        # TODO: FOR A WEBSITE THE FINAL VIDEO WILL BE SAVED AT A DATABASE
        for dir_path in [self.pyframes_path, self.pywork_path, self.pycrop_path]:
            if os.path.exists(dir_path):
                rmtree(dir_path)

