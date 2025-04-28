from flask import Flask, request, render_template, jsonify
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Modeli yükle
model_path = os.path.join(os.path.dirname(__file__), 'model/glasses_cnn_model.h5')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model dosyası bulunamadı: {model_path}")
model = tf.keras.models.load_model(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    if file:
        # Save the uploaded image to static folder for display
        upload_folder = os.path.join(app.static_folder, 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        filename = 'last_upload.jpg'
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        # Process image for prediction
        img = load_img(file_path, target_size=(128, 128))
        img_array = img_to_array(img) / 255.0
        img_array = img_array.reshape((1, 128, 128, 3))

        # Model prediction
        prediction = model.predict(img_array)
        result = "Glasses Detected" if prediction[0][0] < 0.5 else "Glasses Not Detected"

        return render_template('index.html', 
                             result=result, 
                             result_image=f'uploads/{filename}')

@app.route('/')
def index():
    # Clear any existing uploads when starting fresh
    upload_folder = os.path.join(app.static_folder, 'uploads')
    if os.path.exists(upload_folder):
        for file in os.listdir(upload_folder):
            os.remove(os.path.join(upload_folder, file))
    return render_template('index.html', result=None)

@app.route('/clear_image', methods=['POST'])
def clear_image():
    try:
        upload_folder = os.path.join(app.static_folder, 'uploads')
        if os.path.exists(upload_folder):
            for file in os.listdir(upload_folder):
                file_path = os.path.join(upload_folder, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Successfully deleted {file_path}")
        # Cache kontrolü için ek header
        response = jsonify({'status': 'success'})
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response, 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # or any other port number
