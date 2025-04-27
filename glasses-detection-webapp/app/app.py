from flask import Flask, request, render_template
import os
import tempfile
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Modeli yükle
model_path = os.path.join(os.path.dirname(__file__), 'model/glasses_cnn_model.h5')
model = tf.keras.models.load_model(model_path)
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model dosyası bulunamadı: {model_path}")
model = tf.keras.models.load_model(model_path)
@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part", 400  # Dosya yüklenmediyse hata döndür
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400  # Dosya seçilmediyse hata döndür
    if file:
        # Geçici bir dosya oluştur
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            file_path = temp_file.name
            file.save(file_path)

        # Resmi yükle ve modele uygun hale getir
        img = load_img(file_path, target_size=(128, 128))  # Modelin giriş boyutuna göre ayarla
        img_array = img_to_array(img) / 255.0  # Normalizasyon
        img_array = img_array.reshape((1, 128, 128, 3))  # Modelin beklediği şekle getir

        # Model tahmini
        prediction = model.predict(img_array)
        result = "Gözlük VAR" if prediction[0][0] < 0.5 else "Gözlük YOK"

        # Geçici dosyayı sil
        os.remove(file_path)

        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)