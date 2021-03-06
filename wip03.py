#command to install opencv library so that "import cv2" command does not fail
#python -m pip install opencv-python
#python -m pip install numpy

#https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

#from skimage.measure import structural_similarity as ssim
#import matplotlib.pyplot as plt
import numpy as np

import cv2


# import the necessary packages
import argparse
import cv2
import math


def calculateMidpoint(point1,point2):
	x1 = point1[0]
	y1 = point1[1]
	x2 = point2[0]
	y2 = point2[1]

	xDist = math.fabs(x2 - x1)
	yDist = math.fabs(y2 - y1)
	xMid = (x2-math.ceil(xDist/2))
	yMid = (y2-math.ceil(yDist/2))	
	
	return (xMid, yMid)

def calculateDistance(point1,point2):
	x1 = point1[0]
	y1 = point1[1]
	x2 = point2[0]
	y2 = point2[1]

	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return dist
	
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)
		
		

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
filepath="C:/workspaces/AnjutkaVideo/frames/frame1.jpg"

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping, filepath,lineDefined,onePointDefined

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed


	# check to see if the left mouse button was released
	if event == cv2.EVENT_LBUTTONDOWN:
		if not onePointDefined:
			refPt = [(x, y)]
		else:
			refPt.append((x, y))
		cv2.rectangle(image, (x,y), (x+2,y+2), (255, 0, 0), 2)
		cv2.imshow(filepath, image)
		
		if onePointDefined:
			lineDefined = True
		onePointDefined = True
		
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		#refPt.append((x, y))
		#cropping = False

		# draw a rectangle around the region of interest
		#cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		
		if lineDefined:
			lineThickness = 2
			cv2.line(image, refPt[0], refPt[1], (0,255,0), lineThickness)
			cv2.imshow(filepath, image)

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
#image = cv2.imread(args["image"])


image = cv2.imread(filepath)
clone = image.copy()
cv2.namedWindow(filepath)
cv2.setMouseCallback(filepath, click_and_crop)

lineDefined = False
onePointDefined = False
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow(filepath, image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break

# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	
	print "selected ROI"
	print refPt

	print "line length is:"
	print calculateDistance(refPt[0], refPt[1])

	print "center of the line is:"
	print calculateMidpoint(refPt[0], refPt[1])

	
	
	#cv2.imshow("ROI", roi)
	cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()		

