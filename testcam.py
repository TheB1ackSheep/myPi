import cv2
import time
import os 

cv2.namedWindow("Preview",cv2.WINDOW_NORMAL);

while 1:
	os.system("raspistill -o image.jpg")
	image = cv2.imread("image.jpg")
	cv2.imshow("Preview",image)

