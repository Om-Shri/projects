import cv2

video_cap = cv2.VideoCapture(0)
face_cap = cv2.CascadeClassifier("C:/Users/Pramod sah/some projects/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
while True:
    ret , video_data = video_cap.read()
    cv2.imshow("FaceRecognition",video_data)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()