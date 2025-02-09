import warnings


import whisperx
from datetime import timedelta
import re
import os
from datetime import datetime

warnings.filterwarnings("ignore")

class AudioTranscribe:

    def __init__(self, save_path=None, audio_path=None, words_per_line=None):
        super(AudioTranscribe, self).__init__()
        self.segment_length = None
        self.output = []

        self.device = "cuda"
        self.batch_size = 16  # reduce if low on GPU mem
        self.compute_type = "float16"

        # Initialize class parameters
        self.save_path = save_path
        self.audio_path = audio_path
        self.words_per_line = words_per_line

    def transcribe(self, audio_path: str):
        # 1. Transcribe with original whisper (batched)
        model = whisperx.load_model("medium", self.device, compute_type=self.compute_type)
        audio = whisperx.load_audio(audio_path)
        result = model.transcribe(audio, batch_size=self.batch_size)

        # 2. Align whisper output
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)

        return result

    def writeSubtitlesIntoFile(self, input_results: list, output_path: str, words_per_line: int):
        output = []
        self.segment_length = len(input_results)
        cur_segment_words = []
        cur_segment_start = None
        cur_segment_end = None

        for i in range(self.segment_length):
            words = input_results[i]["words"]

            for word_info in words:
                if "start" not in word_info or "end" not in word_info:
                    print(f"Skipping word with missing 'start' or 'end': {word_info}")
                    continue

                word = word_info.get("word", "").strip()  # Avoid KeyError

                if not cur_segment_words:
                    cur_segment_start = word_info["start"]

                cur_segment_words.append(word)

                if len(cur_segment_words) >= words_per_line:
                    cur_segment_end = word_info["end"]
                    output.append({"words": cur_segment_words[:], "start": cur_segment_start, "end": cur_segment_end})
                    cur_segment_words = []
                    cur_segment_start = None
                    cur_segment_end = None

        # Add any remaining words as the last segment
        if cur_segment_words:
            cur_segment_end = words[-1]["end"]
            output.append({"words": cur_segment_words[:], "start": cur_segment_start, "end": cur_segment_end})

        file_content = ""
        for segment in output:
            start_seconds = int(segment["start"])
            start_milliseconds = int((segment["start"] - start_seconds) * 1000)
            start_time = timedelta(seconds=start_seconds, milliseconds=start_milliseconds)

            end_seconds = int(segment["end"])
            end_milliseconds = int((segment["end"] - end_seconds) * 1000)
            end_time = timedelta(seconds=end_seconds, milliseconds=end_milliseconds)

            start_time_str = f"{start_time.seconds//3600:02}:{(start_time.seconds//60)%60:02}:{start_time.seconds%60:02},{start_milliseconds:03d}"
            end_time_str = f"{end_time.seconds//3600:02}:{(end_time.seconds//60)%60:02}:{end_time.seconds%60:02},{end_milliseconds:03d}"

            text = " ".join(segment["words"])
            text = re.sub(f'[.,?"\-!]', '', text).upper()  # Convert text to uppercase & Remove Some Characters
            segment_text = f"{start_time_str} --> {end_time_str}\n{text}\n\n"
            file_content += segment_text

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            f.write(file_content)
            print("File has been written")

    def generate_transcription(self, save_path, audio_path, words_per_line):
        # Locations to save
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        transcript_location = os.path.join(save_path, f"transcript_{timestamp}.srt")

        # Creates the subs in srt file
        self.writeSubtitlesIntoFile(self.transcribe(audio_path)["segments"], transcript_location, words_per_line)
        print(transcript_location)
        return transcript_location

if __name__ == "__main__":
    save_path = r"C:\Users\Alexa\Documents\TikTok-Automation\AutoMedia-Project\CropMedia-Website\backend\src\temp_files"
    audio_path = r"C:\Users\Alexa\Documents\TikTok-Automation\AutoMedia-Project\CropMedia-Website\backend\src\temp_files\video_audio\audio.wav"
    words_per_line = 3
    video_processor = AudioTranscribe(save_path, audio_path, words_per_line)
    video_processor.generate_transcription(save_path, audio_path, words_per_line)
