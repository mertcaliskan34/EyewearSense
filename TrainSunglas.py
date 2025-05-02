import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
# Paths
base_dir = 'data'
img_size = (128, 128)
batch_size = 32
early_stop = EarlyStopping(patience=5, restore_best_weights=True)

# Data generators
train_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    base_dir + '/train',
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary'
)

val_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    base_dir + '/val',
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary'
)

# Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
history = model.fit(train_gen, epochs=30, validation_data=val_gen, callbacks=[early_stop])

# Save
model.save('glasses_type_classifierv3.h5')