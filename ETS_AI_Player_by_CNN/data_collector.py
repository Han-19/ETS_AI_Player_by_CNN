import numpy as np
import PIL
import cv2
import time
from keyboard_events import *
from image_grabber import get_img
import keyboard
import os


def countdown(count_from):
    for i in range(count_from):
        print(count_from - i)
        time.sleep(1)


def key_output():
    a = 0
    w = 0
    d = 0
    if keyboard.is_pressed('a'):
        a = 1
    if keyboard.is_pressed('d'):
        d = 1
    if keyboard.is_pressed('w'):
        w = 1
    if a + d + w == 3:
        return [0, 0, 0]
    return [a, w, d]


file_name = 'training_data_long.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():
    bounding_box = {'top': 100, 'left': 0, 'width': 1024, 'height': 700}

    countdown(4)

    paused = False

    while True:
        if not paused:
            last_time = time.time()
            image = get_img(bounding_box)
            output = key_output()
            training_data.append([image, output])
            if len(training_data) % 1000 == 0:
                print(len(training_data))
                np.save(file_name, training_data)

        if keyboard.is_pressed('t'):
            if paused:
                paused = False
                countdown(3)
                print("Unpaused")
            else:
                print('Paused!')
                paused = True
                time.sleep(1)


main()
