import time
import subprocess
from pathlib import Path
from multiprocessing import Process

from speaker_tracker import LightASD
from audio_transcribe import AudioTranscribe

class VideoManager:
    def __init__(self, video_path, fine_tuned_model=True, n_data_loader_thread=10):
        self.video_path = video_path
        self.fine_tuned_model = fine_tuned_model
        self.n_data_loader_thread = n_data_loader_thread

        # Directories
        self.project_root = Path(__file__).resolve().parent
        self.save_path = self.project_root / "temp_files"
        self.video_assets = self.save_path / "video_audio" 
        self.transcript_assets = self.save_path / "video_transcript"

        # Audio Save Location
        self.audio_file_path = self.video_assets / "audio.wav"  

        # Create directories
        self.save_path.mkdir(parents=True, exist_ok=True)
        self.video_assets.mkdir(parents=True, exist_ok=True)
        self.transcript_assets.mkdir(parents=True, exist_ok=True)

        # Initialize processing modules
        self.asd = LightASD(video_path=self.video_path, fine_tuned_model=self.fine_tuned_model)
        self.audio_transcription = AudioTranscribe()

    def run_command(self, command):
        """Helper function to run a command and capture output/errors."""
        try:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(f"Command Error: {stderr}")
            else:
                print(f"Command Successful.")

        except Exception as e:
            print(f"Exception while running command: {e}")

    def extract_audio(self):
        """Extracts audio from video."""
        command = (
            f"ffmpeg -y -i {self.video_path} -qscale:a 0 -ac 1 -vn -threads {self.n_data_loader_thread} "
            f"-ar 16000 {self.audio_file_path} -loglevel panic"
        )
        print("Extracting Audio...")
        self.run_command(command)

    def track_faces(self):
        """Run face tracking."""
        start = time.time()
        vid_tracks, scores, self.pyframes_path = self.asd.run()
        end = time.time()
        print(f"Face Tracking Elapsed Time: {end - start:.2f} seconds")

    def transcribe_audio(self):
        """Run audio transcription."""
        start = time.time()
        audio_transcription_path = self.audio_transcription.generate_transcription(self.transcript_assets, self.audio_file_path, 3)
        end = time.time()
        print(f"Transcription Elapsed Time: {end - start:.2f} seconds")

    def process_video(self):
        """Process the video: Extract audio, then run face tracking & transcription in parallel."""

        # Step 1: Extract Audio First (Needed for Transcription)
        self.extract_audio()

        # Step 2: Run Face Tracking & Transcription in Parallel
        face_tracking_process = Process(target=self.track_faces)
        transcription_process = Process(target=self.transcribe_audio)

        face_tracking_process.start()
        transcription_process.start()

        face_tracking_process.join()
        transcription_process.join()

        print("Processing Complete!")


if __name__ == "__main__":
    video_path = r"C:\Users\Alexa\Documents\TikTok-Automation\AutoMedia-Project\CropMedia-Website\testVid.mp4"
    video_processor = VideoManager(video_path)
    video_processor.process_video()
