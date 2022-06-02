import cv2
import os
import pytesseract
import pandas as pd
import easyocr
import openpyxl
import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
folder_dir = "SKY2339"
window_name = "image"
reader = easyocr.Reader(['en'], gpu=True)

# img = cv2.imread('SKY2339TARGET-5.jpg')
imglist = []
df = pd.DataFrame({'SKU': [], 'Text': []})

for x in os.listdir(folder_dir):
    if (x.endswith(".jpg")):
        imglist.append("SKY2339/" + x)

print(imglist)

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)

# thresholding
def thresholding(image):
    # return cv2.threshold(image, -20, 20, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

for z in imglist:
    img = cv2.imread(z)
    img = get_grayscale(img)
    img = thresholding(img)
    img = remove_noise(img)
    # cv2.imwrite('/path/' + name + '_fixed.jpg', img)
    # cv2.imwrite(z + ".jpg", img)
    # text = pytesseract.image_to_string(img)
    text = reader.readtext(img, detail=0, paragraph=True)
    df.loc[len(df.index)] = [z, text]
    print("Image: " + z)
    print(text)
    print(df)


df.to_excel("output.xlsx")