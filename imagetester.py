import cv2
import os
import pytesseract
import pandas as pd
#import easyocr
import openpyxl
import glob
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
folder_dir = "SKY2339"
window_name = "image"
# reader = easyocr.Reader(['en'], gpu=True)

img = cv2.imread('SKY2339\SKY2339TARGET-3.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def adaptive_thresh(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)


img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)
# img = adaptive_thresh(img)

# kernel = np.ones((1,1), np.uint8)
# img = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('_fixed.jpg', img)
# cv2.imwrite(z + ".jpg", img)
text = pytesseract.image_to_string(img)
# text = reader.readtext(img, detail=0, paragraph=True)
print(text)