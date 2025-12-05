import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = "IA/IA/Captura/dataset/"

datagen = ImageDataGenerator(
    rescale=1/255.0,
    validation_split=0.2,
)

train_data = datagen.flow_from_directory(
    train_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    train_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode="categorical",
    subset="validation"
)

# Modelo MobileNetV2 preentrenado en ImageNet
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(160, 160, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # Congelado

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(train_data.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(train_data, validation_data=val_data, epochs=10)

model.save("face_cnn_model.h5")
print("Modelo guardado.")
