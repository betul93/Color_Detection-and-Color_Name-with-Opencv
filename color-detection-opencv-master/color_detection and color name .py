#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install --upgrade opencv-python


# In[2]:


# Create the camera capture object
cap = cv2.VideoCapture(0)  # 0, means the first camera on your computer

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Start an endless loop
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If the image was read successfully, continue
    if ret:
        # Show the image on the screen
        cv2.imshow('Camera', frame)

        # Terminate the loop when 'q' key is pressed from the keyboard
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No image received.")
        break

# Release used resources and close windows
cap.release()
cv2.destroyAllWindows()


# In[3]:


import cv2
from PIL import Image

import sys
sys.path.append(r'C:\Users\CASPER\Desktop\face_recog\Yeni klasör\color-detection-opencv-master')
from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
        # Defining the position and font where we will add the text
        position = (x1, y1 - 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (0, 255, 255)  # Yellow color in BGR format
        font_thickness = 2

        # Add text
        cv2.putText(frame, "Yellow", position, font, font_scale, font_color, font_thickness)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


# In[ ]:




