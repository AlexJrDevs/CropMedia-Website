
import json

class SpeakerTracker:
    def __init__(self, talking_tracker):
        super(SpeakerTracker, self).__init__()

        self.talking_tracker = talking_tracker

    def track_speakers(self, video_path):
        data = self.talking_tracker.process(self, video_path)
        face_data = {frame_data.get("frame_number"): frame_data.get("faces", []) for frame_data in data}
        
        with open("data/speaker_labels.json", "w") as f:
            json.dump(face_data, f)

        return face_data