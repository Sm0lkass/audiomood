from analyzer import *
from visualization import plot_waveform
from report import create_pdf_report

audio_path = "C:/Users/k513e/Downloads/propavsaia-gramota.mp3"

y, sr = load_audio(audio_path)

metrics = {
    "duration": analyze_duration(y, sr),
    "lufs": analyze_lufs(y, sr)
}

clipping = analyze_clipping(y, sr)
pauses = analyze_pauses(y, sr)

metrics["clipping_count"] = clipping["count"]
metrics["pause_count"] = len(pauses)

plot_waveform(
    y, sr,
    clipping,
    pauses,
    "waveform.png"
)

create_pdf_report(
    "audio_report.pdf",
    "waveform.png",
    metrics
)
