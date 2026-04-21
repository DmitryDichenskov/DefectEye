import gradio as gr
from ultralytics import YOLO
import os
from flask import Flask, request, jsonify
import threading
import time

# Пути
# Путь к текущему каталогу скрипта
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к модели относительно скрипта
MODEL_PATH = os.path.join(SCRIPT_DIR, "best.pt")
VIDEO_DIR = "/path/to/your/video/folder"  # Укажи путь к папке с видео заранее
SAVE_DIR = "web_results"
os.makedirs(SAVE_DIR, exist_ok=True)

# Загружаем модель один раз
model = YOLO(MODEL_PATH)

# Gradio функция для изображения
def detect_image(img):
    if img is None:
        return None
    results = model.predict(source=img, save=False, verbose=False)
    result_img = results[0].plot()
    save_path = os.path.join(SAVE_DIR, f"web_image_{int(time.time())}.jpg")
    results[0].save(save_path)
    print(f"Изъяны на изображении: {len(results[0].boxes)} объектов")
    return result_img

# Gradio интерфейс
iface = gr.Interface(
    fn=detect_image,
    inputs=gr.Image(type="pil", label="Загрузи фото для анализа изъянов"),
    outputs=gr.Image(type="pil", label="Результат с детекцией"),
    title="Детекция изъянов на металле",
    description="Загружай фото, модель найдет дефекты."
)

# Flask для внешнего пинга видео
app = Flask(__name__)

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    data = request.json
    if not data or 'password' not in data or data['password'] != 'your_secret_password':  # Простая защита
        return jsonify({"error": "Unauthorized"}), 401
    
    if not os.path.exists(VIDEO_DIR):
        return jsonify({"error": "Video directory not found"}), 404
    
    valid_video_exts = (".mp4", ".avi", ".mov", ".mkv", ".webm")
    video_files = [os.path.join(VIDEO_DIR, f) for f in os.listdir(VIDEO_DIR) 
                   if f.lower().endswith(valid_video_exts)]
    
    if not video_files:
        return jsonify({"error": "No videos found"}), 404
    
    # Запускаем анализ в фоне
    thread = threading.Thread(target=process_videos, args=(video_files,))
    thread.start()
    
    return jsonify({"status": "started", "videos": len(video_files)})

def process_videos(video_files):
    for video_path in video_files:
        print(f"Анализ видео: {video_path}")
        results = model.predict(source=video_path, save=True, project=SAVE_DIR, name="video_results", verbose=True)
        print(f"Видео обработано, результаты в {SAVE_DIR}/video_results")

if __name__ == "__main__":
    # Запуск Gradio и Flask параллельно
    gradio_thread = threading.Thread(target=lambda: iface.launch(server_name="0.0.0.0", server_port=7860))
    gradio_thread.start()
    
    print("Gradio UI: http://localhost:7860")
    print("Flask API: http://localhost:5000/analyze_video (POST с JSON {'password': 'your_secret_password'})")
    app.run(host="0.0.0.0", port=5000)