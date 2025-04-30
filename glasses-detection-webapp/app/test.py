import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load models
model_glasses = tf.keras.models.load_model('glasses_cnn_model.h5')
model_type = tf.keras.models.load_model('glasses_type_classifier.h5')

# Image folder
test_dir = 'data/test'  
img_size = (128, 128)

image_files = [f for f in os.listdir(test_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

plt.figure(figsize=(16, 12))

for i, img_name in enumerate(image_files):
    img_path = os.path.join(test_dir, img_name)
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Step 1: Detect if glasses exist
    pred_glasses = model_glasses.predict(img_array)[0][0]
    
    if pred_glasses < 0.5:
        # Glasses detected -> predict type
        pred_type = model_type.predict(img_array)[0][0]
        result = "Sunglasses" if pred_type > 0.5 else "Normal Glasses"
    else:
        result = "No Glasses"

    # Plot
    plt.subplot((len(image_files) + 3) // 4, 4, i + 1)
    plt.imshow(img)
    plt.title(f"{img_name}\n{result}")
    plt.axis('off')

plt.tight_layout()
plt.show()
