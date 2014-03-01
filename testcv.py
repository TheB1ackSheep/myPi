import os
import cv2
import math

def resize(img):
	dst = cv2.resize(img,None,fx=0.25,fy=0.25,interpolation = cv2
.INTER_LINEAR)
	return dst
print "Capturing picture..."
os.system("raspistill -o image.jpg")
print "The picture's been captured"
img = cv2.imread("image.jpg")
img = resize(img)
cv2.namedWindow( "image", cv2.CV_WINDOW_AUTOSIZE );
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
