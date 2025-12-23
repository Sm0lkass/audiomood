'''
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
'''
import matplotlib.pyplot as plt
import librosa.display
from matplotlib.patches import Patch

def plot_waveform(y, sr, clipping, pauses, output_path, legend_loc="upper right"):
    """
    Рисует волновую форму, закрашенные паузы и линии клиппинга,
    и добавляет легенду прямо на изображении.

    Параметры:
      y, sr        - сигнал и частота дискретизации
      clipping     - dict с ключом "times": список времён (в сек.) клиппинга
      pauses       - список dict'ов с "start" и "duration" (в сек.)
      output_path  - путь куда сохранить png
      legend_loc   - позиция легенды (по умолчанию 'upper right')
    """
    # Цвета (согласованы с тем, что используешь в PDF)
    pale_blue = "#ADD8E6"   # Long pauses
    pale_red  = "#FFB3B3"   # Clipping samples

    fig, ax = plt.subplots(figsize=(14, 4))

    # Волнoвая форма
    librosa.display.waveshow(y, sr=sr, alpha=0.9, ax=ax)

    # Закрашенные области — паузы
    for pause in pauses:
        start = pause["start"]
        duration = pause.get("duration", 0)
        ax.axvspan(start, start + duration, facecolor=pale_blue, alpha=0.4, edgecolor=None)

    # Вертикальные линии — клиппинг
    for t in clipping.get("times", []):
        ax.axvline(t, color=pale_red, alpha=0.9, linewidth=0.8)

    # Легенда (маленькие квадратики)
    handles = [
        Patch(facecolor=pale_blue, edgecolor='none', alpha=0.4, label="Long pauses"),
        Patch(facecolor=pale_red,  edgecolor='none', alpha=0.9, label="Clipping samples")
    ]
    legend = ax.legend(handles=handles, loc=legend_loc, framealpha=0.92, fontsize=9, fancybox=True)
    # чуть стилизуем рамку легенды
    frame = legend.get_frame()
    frame.set_linewidth(0.5)
    frame.set_edgecolor("#cccccc")

    ax.set_title("Waveform with Clipping and Pauses")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
