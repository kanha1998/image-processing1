
import cv2
import numpy as np  

img = cv2.imread('lineimage.jpg')

lower_color = np.array([110,100,100])
upper_color = np.array([130,255,255])

# blue color segmention
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,lower_color,upper_color)

cv2.imshow('mask',mask)

res = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
