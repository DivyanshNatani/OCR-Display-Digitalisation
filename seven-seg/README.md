## Jupyter Notebooks
This folder contains all the jupyter notebooks in which the seven segment algorithms are tried out. For more information on seven-seg, please read [report](../Presentation.pdf)

- temprature_instrument_detail.ipynb : This file contains the algorithm to identify bounding box of the screen display from the instrument, then finding the digit bounding box in the screen display and then identifing the digit from the bounding box using seven-segment technique. This code is motivated from [pyimagesearch article](https://pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/). temprature_instrument.ipynb contains compressed code of same file

- temprature_reading_algo_on_lab_image.ipynb : the above algorithm is used on lab image, but it does not work as it is not able to identify digit bounding box in screen display because of high black disturbance in display

- Lab_image_seven_segment_recognition.ipynb : this file uses manual bounding box of digit to recoganise digits in the lab image

- printed_image_with_function.iypnb : This file uses printed images scanned from IP Camera and uses above algorithm(with manual bounding box) to identify digits. Other printing_image___ files contain static versions(not connected to IP Camera) of same file

### Python packages required
These files use imutils, cv2 packages along with matplotlib and numpy libraries
```
pip install imutils
```
