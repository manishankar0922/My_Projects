
#some open cv basic operations

import cv2
import numpy as np

im = cv2.imread('opencvBasics\\AdobeStock_722574144_Preview[1].jpeg')

        #        variable,width,height
resized = cv2.resize(im ,(400,400))

gray_scale = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

blank = np.zeros((400,400),dtype='uint8')

react = cv2.rectangle(blank,(30,30),(370,370),(255,255,255),thickness=2)
cir = cv2.circle(react,(50,50),30,(255,255,255),2)

save = cv2.imwrite('opencvBasics\\new_image.jpg',cir)

if save is False:
    print("chusuko")
else:
    print("image saved")


if im is None:
    print("am leh dolla")
else:
    cv2.imshow('gray_scale', gray_scale)
    cv2.imshow("resized", resized)
    cv2.imshow('1st_im', im)
    cv2.imshow('blank', cir)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

