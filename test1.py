from PIL import Image
import cv2
import pytesseract

print("Hello")

im=Image.open("data/1.jpg")
print(im)
# im.show()

im.save("output/1.jpg")