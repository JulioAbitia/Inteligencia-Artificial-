import cv2
import numpy as np
import tensorflow as tf
import os

# Cargar modelo
model = tf.keras.models.load_model("face_cnn_model.h5")

# Cargar nombres de clases (personas)
class_names = sorted(os.listdir("IA/IA/Captura/dataset"))
print("Clases:", class_names)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_frontalface_default.xml")


def preprocess_face(face_img):
    face_img = cv2.resize(face_img, (160,160))
    face_img = face_img.astype("float32") / 255.0
    return np.expand_dims(face_img, axis=0)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]
        pre = preprocess_face(face)

        preds = model.predict(pre, verbose=0)[0]
        class_id = np.argmax(preds)
        confidence = preds[class_id]

        # Establecer confianza mínima
        if confidence < 0.60:
            name = "Desconocido"
        else:
            name = class_names[class_id]

        # Dibujar detección
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f"{name} ({confidence*100:.1f}%)",
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0,255,0), 2)

    cv2.imshow("Reconocimiento Facial", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
