
#only face detection


import cv2 

test = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


image = cv2.imread('opencvBasics/download.jpg')


if image is None:
    print('am leh dolla')
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = test.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(40, 40))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

# rez = cv2.resize(image,(1400,10000))


cv2.imshow('Face Detection', image)
def_ = cv2.waitKey(0)

if def_ == ord('1'):
    
    cv2.destroyAllWindows()
