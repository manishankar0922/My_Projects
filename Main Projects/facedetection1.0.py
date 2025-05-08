
#face and hand detection



import cv2
import mediapipe as mp

mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

hands = mphands.Hands()

test = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('CHUSUKO RA GOLLIGA')
    exit()

else:
    while cap.isOpened():
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGRA)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hands_landmark in results.multi_hand_landmarks:
                mpdraw.draw_landmarks(frame,hands_landmark,mphands.HAND_CONNECTIONS)

        faces = test.detectMultiScale(rgb_frame, scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        for (x, y, w, h) in faces:
            #cv2.circle(frame,(x+w//2,y+h//2),w//2,(255,10,0),1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if not ret:
            print("cam break ra golliga")
            break
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('1'):
            break
    cap.release()
    cv2.destroyAllWindows()