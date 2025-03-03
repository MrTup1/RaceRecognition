import cv2
import threading
from deepface import DeepFace

cap = cv2.VideoCapture(0)


counter = 0
face_match = False
race = "Alien"
#referenceImg = cv2.imread("reference.jpg")

"""def checkFace(frame): # Checks if face in webcam matches an input image
    global face_match
    try:
        if DeepFace.verify(frame, referenceImg.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False"""

def checkRace(frame): #Checks for the highest probable race in webcam
    global race
    try:
        rawData = DeepFace.analyze(frame, "race")
        race =  rawData[0]['dominant_race']

    except ValueError:
        race = "no race"

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target = checkRace(frame), args = (frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1
        
        #RACE OUTPUTS
        if (race == "asian"):
            cv2.putText(frame, "GET BACK TO THE RICE FIELDS!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 204, 255), 3)
        elif(race == "indian"):
            cv2.putText(frame, "HELLO YOUR COMPUTER HAS VIRUS", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (37, 47, 81), 3)
        elif(race == "black"):
            cv2.putText(frame, "I CAN BREATHE NIGGA", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        elif(race == "white"):
            cv2.putText(frame, "SIEG HEIL GAS THEM IMMIGRANTS", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (221, 221, 221), 3)
        elif(race == "middle eastern"):
            cv2.putText(frame, "Allahu Akbar 911 BEST DAY", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (8, 0, 255), 3)
        elif(race == "latino hispanic"):
            cv2.putText(frame, "I LOVE THE SMELL OF COKE", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 95, 191), 3)
        else:
            cv2.putText(frame, "No face detected", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
        
        #VERIFICATION OUTPUTS
        """if face_match:
            cv2.putText(frame, "Welcome Chink", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "No rice eater!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0 , 0), 3)
        """
        cv2.imshow("Frame", frame) #Display image

    key = cv2.waitKey(1)
    if key == 27: #Escape key
        break

cap.release()
cv2.destroyAllWindows()


