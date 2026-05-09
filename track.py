#import the necessary packages
import numpy as np
import argparse 
import cv2

# initialize the current frame of the video, along with the list of
# ROI points along with whether or not this is input mode
frame = None
roiPits = []
inputMode = False

def selectROI(event, x, y, flags, param):
    # grab the reference to the current frame, list of ROI
    # points and whether or not it is ROI selection mode
    global frame, roiPits, inputMode

    # if we are in ROI selection mode, the mouse was clicked
    # and we do not already have four points, then update the
    # list of ROI points with the (x, y) location of the click
    # and draw the circle
    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPits) < 4:
        roiPits.append((x, y))
        cv2.circle(frame, (x,y), 4, (0, 255, 0), 2)
        cv2.imshow("frame", frame)
 
