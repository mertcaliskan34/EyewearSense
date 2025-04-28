from flask import Flask, request, render_template, jsonify
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import uuid
import time

app = Flask(__name__)

# Modeli yükle
model_path = os.path.join(os.path.dirname(__file__), 'model/glasses_cnn_model.h5')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model dosyası bulunamadı: {model_path}")
model = tf.keras.models.load_model(model_path)

# Define the upload folder path
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    if file:
        # Ensure upload folder exists
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        # Generate a unique filename
        _, ext = os.path.splitext(file.filename) # Get original extension
        if not ext: # Default extension if none provided
             ext = '.jpg'
        filename = f"{uuid.uuid4()}{ext}" # Create unique name like 'uuid.ext'
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        print(f"Saved image to: {file_path}") # Debugging output

        # Process image for prediction
        try:
            img = load_img(file_path, target_size=(128, 128))
            img_array = img_to_array(img) / 255.0
            img_array = img_array.reshape((1, 128, 128, 3))

            # Model prediction
            prediction = model.predict(img_array)
            result = "Glasses Detected" if prediction[0][0] < 0.5 else "Glasses Not Detected"

            # Construct the image URL relative to the static folder
            result_image_url = f'uploads/{filename}'

            # Add a cache-busting query parameter (optional but good practice)
            # result_image_url_with_cache = f'{result_image_url}?v={int(time.time())}'

            return render_template('index.html',
                                 result=result,
                                 result_image=result_image_url) # Pass the unique relative path
                                 # result_image=result_image_url_with_cache) # If using cache busting

        except Exception as e:
             # Handle potential errors during image processing or prediction
             print(f"Error processing image or predicting: {e}")
             # Optionally delete the saved file if processing failed
             if os.path.exists(file_path):
                 os.remove(file_path)
             # Render template with an error message
             return render_template('index.html', error_message=f"Error processing image: {e}", result=None)


@app.route('/')
def index():
    # NOTE: Clearing the upload folder on every '/' request might be too aggressive
    # if you want the gallery images to persist across server restarts or browser sessions
    # without relying solely on localStorage. Consider commenting this out if persistence
    # of the actual files is desired beyond the current session.
    # upload_folder = os.path.join(app.static_folder, 'uploads')
    # if os.path.exists(upload_folder):
    #     for file_in_dir in os.listdir(upload_folder):
    #         os.remove(os.path.join(upload_folder, file_in_dir))
    return render_template('index.html', result=None)

@app.route('/clear_image', methods=['POST'])
def clear_image():
    # This route should now primarily be used by the gallery's "Clear All"
    # It will delete ALL files in the uploads folder.
    try:
        if os.path.exists(UPLOAD_FOLDER):
            deleted_count = 0
            for file_to_delete in os.listdir(UPLOAD_FOLDER):
                file_path_to_delete = os.path.join(UPLOAD_FOLDER, file_to_delete)
                if os.path.isfile(file_path_to_delete):
                    os.remove(file_path_to_delete)
                    deleted_count += 1
            print(f"Successfully deleted {deleted_count} file(s) from {UPLOAD_FOLDER}")
        else:
            print(f"Upload folder {UPLOAD_FOLDER} does not exist.")

        response = jsonify({'status': 'success'})
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response, 200
    except Exception as e:
        print(f"Error during clear_image: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Ensure upload folder exists on startup
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, port=5001)
