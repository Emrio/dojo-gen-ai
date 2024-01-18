import os
import openai
import tempfile

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_transcription(audio: bytes) -> str:
  with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
    fp.write(audio)
    fp.seek(0)

    transcript = openai.Audio.transcribe("whisper-1", file=fp)

  os.unlink(fp.name)

  return transcript['text']
