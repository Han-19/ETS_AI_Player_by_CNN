import keyboard
import time

counter_start = 0

keys = {'a_count': 0, 'd_count': 0, 'w_count': 0,
        'a_wanted': 0, 'd_wanted': 0, 'w_wanted': 0,
        'a_cd': 0, 'd_cd': 0, 'w_cd': 0,
        'a_cooled': 0, 'd_cooled': 0, 'w_cooled': 0,
        'a_can_press': 1, 'd_can_press': 1, 'w_can_press': 1}

'''
def is_pressed_enough(func):
    def wrapper(my_key, my_count=0.01, cooldown=0.05):
        counted = time.time() - counter_start
        count = my_count
        my_keys = func(my_key, my_count)
        if (counted - keys[my_key + '_count']) > keys[my_key + '_wanted']:
            keyboard.release(my_key)
            keys[my_key + '_count'] = 0
            keys[my_key + '_cooled'] = time.time()
            keys[my_key + '_can_press'] = 0
        if (counted - keys[my_key + '_cooled']) > keys[my_key + '_cd']:
            keys[my_key + '_can_press'] = 1

    return wrapper


@is_pressed_enough'''


def press(my_key, my_count=0.001, cooldown=0.05):
    if keys[my_key + '_can_press']:
        keyboard.press(my_key)
        keys[my_key + '_count'] = time.time()
        keys[my_key + '_wanted'] = my_count
        keys[my_key + '_cd'] = cooldown
    return keys


def straight():  # [0,1,0]
    press('w')
    keyboard.release('d')
    keyboard.release('a')


def left():  # [1,0,0]
    press('a')
    keyboard.release('d')
    time.sleep(0.005)
    keyboard.release('a')
    time.sleep(0.005)


def right():  # [0,0,1]
    press('d')
    keyboard.release('a')

    time.sleep(0.005)
    keyboard.release('d')
    time.sleep(0.005)


def straight_left():  # [1,1,0]
    press('a')
    press('w')
    keyboard.release('d')


def straight_right():  # [0,1,1]
    press('d')
    press('w')
    keyboard.release('a')
