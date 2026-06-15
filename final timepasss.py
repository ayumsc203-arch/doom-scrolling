import cv2
from ultralytics import YOLO
import pygame

# Load YOLO model
model = YOLO("yolov8n.pt")

# Initialize sound
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\ayums\OneDrive\Desktop\extrapp\wow (3).wav")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    phone_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "cell phone":
                phone_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,"Phone Detected",(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    if phone_detected and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

    cv2.imshow("Phone Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()