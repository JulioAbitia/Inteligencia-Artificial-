import tensorflow as tf
from tensorflow.keras import layers, models  #Libreria para crear y entrenar redes neuronales
import matplotlib.pyplot as plt   #Graficar las curvas de precision

# 1. Cargar dataset de mamografías 
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "mamografias/train",
    image_size=(224, 224),
    batch_size=32
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "mamografias/val",
    image_size=(224, 224),
    batch_size=32
)

# 2. Normalizar imágenes
normalization_layer = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

 

# 3. Crear el modelo CNN 
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(224,224,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")  # salida binaria
])

# 4. Compilar
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# 5. Entrenar el modelo
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)

# 6. Graficar resultados
plt.plot(history.history["accuracy"], label="Precisión entrenamiento")
plt.plot(history.history["val_accuracy"], label="Precisión validación")
plt.legend()
plt.show()

# 7. Ejemplo de predicción
import numpy as np
from tensorflow.keras.preprocessing import image

img = image.load_img("mamografia_nueva.jpg", target_size=(224,224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

pred = model.predict(img_array)

if pred[0][0] > 0.5:
    print("Posible cáncer detectado.")
else:
    print("No se detectan signos de cáncer.")
