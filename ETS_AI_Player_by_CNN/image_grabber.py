# https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python  # getting screen image

import numpy as np
import cv2
from mss import mss
import time


def get_img(bounding_box):  # bounding_box = {'top': 100, 'left': 0, 'width': 1024, 'height':700}
    mss_object = mss()
    sct_img = mss_object.grab(bounding_box)
    original_img = np.array(sct_img)
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.resize(processed_img, (160, 120))
    return processed_img
