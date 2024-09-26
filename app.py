import whisper
import sys

model = whisper.load_model("medium")
result = model.transcribe("ZOOM0015.WAV")
print(result["text"])
