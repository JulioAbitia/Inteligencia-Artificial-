import cv2
import os
//q se guarde en la carpeta correspondiente
nombre = input("Nombre de la persona: ")
output_path = f"IA/IA/Captura/dataset"

os.makedirs(output_path, exist_ok=True)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (160, 160))

        count += 1
        cv2.imwrite(f"{output_path}/{count}.jpg", rostro)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, f"Capturando: {count}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0), 2)

    cv2.imshow("Captura de Rostros", frame)

    if cv2.waitKey(1) == 27 or count >= 400:  # ESC o 100 fotos
        break

cap.release()
cv2.destroyAllWindows()
