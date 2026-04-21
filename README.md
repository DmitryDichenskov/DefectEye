<img width="368" height="221" alt="image" src="https://github.com/user-attachments/assets/01a87d32-726c-4b9d-8309-68f47d318d68" />Детекция изъянов на металле 🚀
Автоматическая система обнаружения дефектов на металлических поверхностях с использованием YOLO11 и Gradio UI

✨ Особенности
🔍 Интерактивный веб-интерфейс — загружайте фото и получайте результаты детекции мгновенно

🎥 Обработка видео — API для пакетного анализа видео файлов

⚡ Высокая производительность — модель загружается один раз, обработка в реальном времени

💾 Автосохранение — результаты сохраняются в удобном формате

🛡️ Простая авторизация — защита API паролем

📱 Доступно везде — Gradio UI и Flask API на разных портах

🛠 Технологии

🤖 YOLO11 (Ultralytics)    # Детекция объектов

🎨 Gradio                 # Веб-интерфейс

⚗️ Flask                  # REST API

📁 Python 3.8+           # Язык разработки

🚀 Быстрый старт
1. Установка зависимостей
   
pip install gradio ultralytics flask opencv-python

2. Подготовка

📁 your_project/

├── best.pt              # Ваша обученная модель YOLO

├── app.py              # Основной скрипт

└── /path/to/your/video/folder/  # Папка с видео (укажите путь)

3. Запуск

python app.py
4. Доступ к интерфейсам
text
🌐 Gradio UI: http://localhost:7860
🔌 API:       http://localhost:5000/analyze_video
🎮 Использование
Gradio UI (Фото)
Откройте http://localhost:7860

Загрузите фото металлической поверхности

Получите результат с bounding boxes дефектов

Результат автоматически сохраняется в web_results/

Flask API (Видео)
bash
curl -X POST http://localhost:5000/analyze_video \
  -H "Content-Type: application/json" \
  -d '{"password": "your_secret_password"}'
Ответ:

json
{
  "status": "started",
  "videos": 3
}
Результаты сохраняются в web_results/video_results/

⚙️ Конфигурация
Параметр	Описание	По умолчанию

MODEL_PATH	Путь к модели YOLO	best.pt

VIDEO_DIR	Папка с видео	/path/to/your/video/folder

SAVE_DIR	Папка результатов	web_results/

PASSWORD	Пароль API	your_secret_password
    
🔍 Поддерживаемые форматы видео
.mp4

.avi

.mov

.mkv

.webm
