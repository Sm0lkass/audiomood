import matplotlib.pyplot as plt
import librosa.display

def plot_waveform(y, sr, clipping, pauses, output_path):
    plt.figure(figsize=(14, 4))

    librosa.display.waveshow(y, sr=sr, alpha=0.6)

    for t in clipping["times"]:
        plt.axvline(t, color='red', alpha=0.1)

    for pause in pauses:
        plt.axvspan(
            pause["start"],
            pause["start"] + pause["duration"],
            color='blue',
            alpha=0.2
        )

    plt.title("Waveform with Clipping and Pauses")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
