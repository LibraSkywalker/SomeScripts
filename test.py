import pyautogui as controller
from PIL import Image,ImageChops
import time
import numpy
import cv2
import os

time1 = time.time()

img1 = controller.screenshot(region=(0, 0, 1920, 1080))
image = cv2.cvtColor(numpy.asarray(img1), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = []
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,20,param1=50,param2=40,minRadius=23,maxRadius=25)
circles = numpy.uint16(numpy.around(circles))

time2 = time.time()
print("time consume:",time2 - time1)
print("result:")
print(circles)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
	
cv2.imwrite('grey.jpg',gray)
cv2.imwrite('result.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
