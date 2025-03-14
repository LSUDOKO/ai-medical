import os
import sounddevice as sd
import numpy as np
import wave
import tempfile
import whisper

def record_audio(duration=5, fs=44100):
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    return audio_data

def save_audio_to_file(audio_data, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(44100)
        wf.writeframes(audio_data.tobytes())

def transcribe_with_groq(GROQ_API_KEY, audio_filepath, stt_model="whisper-large-v3"):
    model = whisper.load_model(stt_model)
    audio = whisper.load_audio(audio_filepath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    options = whisper.DecodingOptions(language="en")
    result = whisper.decode(model, mel, options)
    return result.text.strip()