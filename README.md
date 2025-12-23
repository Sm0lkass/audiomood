# Audio Quality Analyzer

Анализатор качества аудиофайлов на Python.

Проект определяет:
- среднюю громкость (LUFS)
- клиппинг (перегруз)
- длительные паузы (тишина)
- общую длительность
- визуализирует проблемные зоны
- формирует PDF-отчёт

## Возможности
- Поддержка MP3 / WAV
- Волновая форма с отмеченным клиппингом и паузами
- PDF-отчёт с таблицей метрик

## Установка

```bash
git clone https://github.com/USERNAME/audiomood.git
cd audiomood
pip install -r requirements.txt
