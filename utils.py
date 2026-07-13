import config
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model(config.MODEL_PATH)


def predict_class(image_path):

    img = load_img(
        image_path,
        target_size=config.IMAGE_SIZE
    )

    image_array = img_to_array(img)

    image_array = image_array / 255.0

    test_array = tf.expand_dims(image_array, axis=0)

    pred_prob = model.predict(test_array, verbose=0)[0][0]

    confidence = pred_prob

    if pred_prob >= 0.5:
        prediction = "Car"
    else:
        prediction = "Bike"

    return prediction, confidence