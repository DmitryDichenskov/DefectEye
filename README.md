Детекция изъянов на металле 🚀
Автоматическая система обнаружения дефектов на металлических поверхностях с использованием YOLO11 и Gradio UI

✨ Особенности
🔍 Интерактивный веб-интерфейс — загружайте фото и получайте результаты детекции мгновенно

🎥 Обработка видео — API для пакетного анализа видео файлов

⚡ Высокая производительность — модель загружается один раз, обработка в реальном времени

💾 Автосохранение — результаты сохраняются в удобном формате

🛡️ Простая авторизация — защита API паролем

📱 Доступно везде — Gradio UI и Flask API на разных портах

🛠 Технологии
text
🤖 YOLO11 (Ultralytics)    # Детекция объектов
🎨 Gradio                 # Веб-интерфейс
⚗️ Flask                  # REST API
📁 Python 3.8+           # Язык разработки

🚀 Быстрый старт
1. Установка зависимостей
bash
pip install gradio ultralytics flask opencv-python

2. Подготовка
text
📁 your_project/
├── best.pt              # Ваша обученная модель YOLO
├── app.py              # Основной скрипт
└── /path/to/your/video/folder/  # Папка с видео (укажите путь)
3. Запуск
bash
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
📁 Структура результатов
text
web_results/
├── web_image_1234567890.jpg     # Результаты фото
└── video_results/
    ├── video1/
    │   ├── video1.mp4
    │   ├── video1_pred.jpg
    │   └── labels/
    └── video2/
        └── ...
🔍 Поддерживаемые форматы видео
.mp4

.avi

.mov

.mkv

.webm

📞 Контакты
Автор: TheKodDima
Email: your.email@example.com
GitHub: github.com/yourusername
