import cv2
###from deepface import DeepFace

cap = cv2.VideoCapture(0)


counter = 0
face_match = False

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


