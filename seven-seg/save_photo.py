import cv2

import requests

url = 'http://192.168.0.102:8080/photoaf.jpg'
page = requests.get(url)

f_ext = '_myimg'
f_name = 'saved_photos/img{}.jpg'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)
    print("Image Accessed")