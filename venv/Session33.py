import cv2
import pytesseract

img = cv2.imread("data.png",cv2.IMREAD_COLOR)
print(type(img))

text = pytesseract.image_to_string(img,lang="eng")
print(text)