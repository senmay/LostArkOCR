# imports:
import cv2
import os
import numpy as np
# OCR imports:
from PIL import Image
import pyocr
import pyocr.builders

# image path
path = "J://programowanie//ocrpy//"
fileName = "processed_screenshot.png"

# Reading an image in default mode:
inputImage = cv2.imread(path + fileName)

# Get local maximum:
kernelSize = 5
maxKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelSize, kernelSize))
localMax = cv2.morphologyEx(inputImage, cv2.MORPH_CLOSE, maxKernel, None, None, 1, cv2.BORDER_REFLECT101)

# Perform gain division
gainDivision = np.where(localMax == 0, 0, (inputImage/localMax))

# Clip the values to [0,255]
gainDivision = np.clip((255 * gainDivision), 0, 255)

# Convert the mat type from float to uint8:
gainDivision = gainDivision.astype("uint8")

outputFileName = "output_image.png"
cv2.imwrite(path + outputFileName, gainDivision)