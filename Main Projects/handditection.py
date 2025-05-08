
#only bhand detection


import cv2
import mediapipe as mp 

mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

hands = mphands.Hands()

cap = cv2.VideoCapture(0)

if cap is True:
    print("works")

while cap.isOpened():
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(gray)
    
    #the main thing 
    if results.multi_hand_landmarks: #multi hands vunnaya leva ani chudadaniki   
        for hand_landmark in results.multi_hand_landmarks: #each hands ni detect chy daniki 
            mpdraw.draw_landmarks(frame,hand_landmark,mphands.HAND_CONNECTIONS) #ah hands ki manam marks pett daniki 

    frame = cv2.flip(frame, 1)
    if not ret:
        print("cap ki amtey ")
        break

    cv2.imshow('hand detection',frame)
    if cv2.waitKey(1) == ord('1'):
        print("video was closed..1")
        break

cap.release()
cv2.destroyAllWindows()