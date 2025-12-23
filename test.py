import librosa
import librosa.display
import IPython.display as ip
import matplotlib.pyplot as plt
import numpy as np
import os
import pyloudnorm as pyln

CLIP_THRESHOLD = 0.99
LENGTH_OF_PAUSE = 1.5

#audio_path = 'C:/Users/k513e/Downloads/Soldiers_Eyes.mp3'
audio_path = 'C:/Users/k513e/Downloads/kastanka.mp3'

# Проверка существования файла
if os.path.exists(audio_path):
    print(f"Файл найден: {audio_path}")

    y, sr = librosa.load(audio_path, sr=None, mono=True)

    # Расчет LUFS
    meter = pyln.Meter(sr)  # создаем измеритель LUFS
    loudness = meter.integrated_loudness(y)
    print(f"Средняя громкость LUFS: {loudness:.2f} LUFS")

    #Продолжительность файла
    duration_sec = len(y) / sr
    print(f"Длительность:{duration_sec:.2f} сек")

    #Клиппинг
    clipped_samples = np.where(np.abs(y) >= CLIP_THRESHOLD)[0]
    clip_count = len(clipped_samples)
    print(f"Количество клиппинг-отсчётов: {clip_count}")
    clip_times = clipped_samples / sr
    plt.figure(figsize=(14, 4))

    librosa.display.waveshow(y, sr=sr, alpha=0.6)

    plt.title("Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    for t in clip_times:
        plt.axvline(t, color='red', alpha=0.1)

    #Паузы
    intervals = librosa.effects.split(
        y,
        top_db = 40
    )
    pauses = []
    for i in range(1, len(intervals)):
        prev_end = intervals[i - 1][1]
        curr_start = intervals[i][0]

        pause_duration = (curr_start - prev_end) / sr

        if pause_duration >=LENGTH_OF_PAUSE:

            pause_start = prev_end / sr
            pause_end = curr_start / sr

            plt.axvspan(
            pause_start,
            pause_end,
            color='blue',
            alpha=0.2
            )
            pauses.append({'Начало паузы': pause_start,
            'Длительность': pause_duration
            })
    print(f"Длинных пауз (>2 сек): {len(pauses)}")
    if len(pauses) > 0:
            print("Паузы:")
            for i, pause in enumerate(pauses, start=1):
                print(
                    f"  {i}. Начало: {pause['Начало паузы']:.2f} сек, "
                    f"длительность: {pause['Длительность']:.2f} сек"
                )


else:
    print(f"Файл не найден: {audio_path}")
    # Проверьте путь, может быть нужно использовать:
    # audio_path = 'C:\\Users\\k513e\\Downloads\\Soldiers_Eyes.mp3'

plt.title("Waveform with Clipping and Pauses")
plt.tight_layout()
plt.show()
