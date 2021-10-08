import numpy as np
import cv2
import time
from alexnet import alexnet
from image_grabber import get_img
from keyboard_events import *
import keyboard

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'ets2_big-car-fast-{}-{}-{}-epochs-300K-data2.model'.format(LR, 'alexnetv2', EPOCHS)

t_time = 0.09

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def countdown(count_from):
    for i in range(count_from):
        print(count_from - i)
        time.sleep(1)


def main():
    bounding_box = {'top': 100, 'left': 0, 'width': 1024, 'height': 700}
    # real full screen  --->  bounding_box = {'top': 40, 'left': 0, 'width': 1024, 'height': 800}
    countdown(4)
    last_time = time.time()

    paused = False
    while True:

        if not paused:
            last_time = time.time()
            image = get_img(bounding_box)
            print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            screen = cv2.resize(image, (160, 120))

            prediction = model.predict([screen.reshape(160, 120, 1)])[0]
            print(prediction)

            turn_thresh = .75
            fwd_thresh = 0.70

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                straight()

            keyboard.press('w')
        if keyboard.is_pressed('t'):
            if paused:
                paused = False
                countdown(3)
                print('Unpaused!')
            else:
                print('Paused!')
                paused = True
                keyboard.release('w')
                time.sleep(1)
        cv2.imshow('window', image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
