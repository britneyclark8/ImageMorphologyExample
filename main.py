# Britney Clark
# Critical Thinking 5
# CSC515: Foundations of Computer Vision
# Dr. Joseph Issa
# February 20, 2022

import cv2
import numpy as np

# Import the image and scale it
img = cv2.imread(r'C:\Users\Stardust\Downloads\LatentFingerprint.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale_percent = 1.5  # percent of original size
width = int(grayimg.shape[1] * scale_percent)
height = int(grayimg.shape[0] * scale_percent)
dim = (width, height)
# resize image
resized = cv2.resize(grayimg, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.imshow('Grey Image', grayimg)
cv2.waitKey(0)

# Erode Image
erosion = cv2.erode(resized, (3, 3), iterations=3)
cv2.imshow('Eroded Image', erosion)
cv2.waitKey(0)

# Dilate Image
dilation = cv2.dilate(resized, (3, 3), iterations=3)
cv2.imshow('Dilated Image', dilation)
cv2.waitKey(0)

# Open Image
opening = cv2.morphologyEx(resized, cv2.MORPH_OPEN, (7, 7))
cv2.imshow('Opened Image', opening)
cv2.waitKey(0)

# Close Image
closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, (7, 7))
cv2.imshow('Closed Image', closing)
cv2.waitKey(0)


