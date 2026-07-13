import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "car_bike_classifier.keras")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

IMAGE_SIZE = (224, 224)

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000