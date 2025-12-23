import librosa
import numpy as np
import pyloudnorm as pyln
from config import CLIP_THRESHOLD, LENGTH_OF_PAUSE, SILENCE_DB

def load_audio(path):
    y, sr = librosa.load(path, sr=None, mono=True)
    return y, sr

def analyze_lufs(y, sr):
    meter = pyln.Meter(sr)
    return meter.integrated_loudness(y)

def analyze_duration(y, sr):
    return len(y) / sr

def analyze_clipping(y, sr):
    clipped = np.where(np.abs(y) >= CLIP_THRESHOLD)[0]
    return {
        "count": len(clipped),
        "times": clipped / sr
    }

def analyze_pauses(y, sr):
    intervals = librosa.effects.split(y, top_db=SILENCE_DB)
    pauses = []

    for i in range(1, len(intervals)):
        pause_duration = (intervals[i][0] - intervals[i-1][1]) / sr
        if pause_duration >= LENGTH_OF_PAUSE:
            pauses.append({
                "start": intervals[i-1][1] / sr,
                "duration": pause_duration
            })

    return pauses
