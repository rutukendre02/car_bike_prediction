from flask import Flask, render_template, request  # type: ignore
import os
import config
from src.utils import predict_class

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(
        config.UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    # Predict
    prediction, confidence = predict_class(filepath)

    confidence = round(confidence * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image=file.filename
    )


if __name__ == "__main__":
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=True
    )
        
    
           
           
           

