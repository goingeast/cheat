# -*- coding: utf-8 -*-
import os
import shutil
import time
import math
import random
import json
from PIL import Image, ImageDraw
import wda
from enum import Enum
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt



VERSION = "0.0.1"
c = wda.Client()
s = c.session()
print("设备尺寸", s.window_size())
print s.orientation
s.orientation = wda.LANDSCAPE
screenshot_backup_dir = 'screenshot_backups/'

if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)


def pull_screenshot():
    c.screenshot('1.png')


def jump(distance):
    press_time = 1000
    print('press time: {}'.format(press_time))
    s.tap_hold(random.uniform(0, 320), random.uniform(64, 320), press_time)

def press_quest():
    print("Quest button pressed")
    s.tap_hold(40 , 390, 0.5)
    time.sleep(random.uniform(0.9, 1.5))
    #s.tap_hold(30,30, 0.5)
    #time.sleep(random.uniform(0.9, 1.5))
   # s.tap_hold(80, 360, 0.5)
def press_back():
    print("Back button pressed")
    s.tap(30, 30)
    time.sleep(random.uniform(0.5, 1.0))

def go_to_quest(number):
    print("Go to Quest button pressed")
    s.tap_hold(500, 100+number*80, 0.5)
    time.sleep(random.uniform(0.9, 1.5))
    s.tap_hold(368, 252, 0.5)
    

def press_rank():
    print("Map button pressed")
    s.tap(500, 390)
    time.sleep(random.uniform(0.9, 1.5))
    s.tap_hold(30,30, 0.5)
    time.sleep(random.uniform(0.9, 1.5))

def press_map():
    print("Map button pressed")
    s.tap_hold(120, 390, 0.5)
    time.sleep(random.uniform(0.9, 1.5))
    s.tap_hold(30,30, 0.5)
    time.sleep(random.uniform(0.9, 1.5))

def press_home():
    print("Home button pressed")
    s.tap_hold(200, 390, 0.5)
    time.sleep(random.uniform(0.9, 1.5))
    s.tap_hold(30,30, 0.5)
    time.sleep(random.uniform(0.9, 1.5))

def press_up_left():
    print("up left pressed")
    s.tap(380-70, 200-70)
    time.sleep(random.uniform(0.9, 1.5))

def press_up_right():
    print("down right pressed")
    s.tap(380+70, 200-70)
    time.sleep(random.uniform(0.9, 1.5))

def press_down_left():
    print("left down pressed")
    s.tap(380-70, 200+70)
    time.sleep(random.uniform(0.9, 1.5))

def press_down_right():
    print("right up pressed")
    s.tap(380+70, 200+70)
    time.sleep(random.uniform(0.9, 1.5))

def press_up():
    print("up pressed")
    s.tap(380, 200-80)
    time.sleep(random.uniform(0.9, 1.5))

def press_down():
    print("down pressed")
    s.tap(380, 200+80)
    time.sleep(random.uniform(0.9, 1.5))

def press_left():
    print("left pressed")
    s.tap(380-80, 200)
    time.sleep(random.uniform(0.9, 1.5))

def press_right():
    print("right pressed")
    s.tap(380+80, 200)
    time.sleep(random.uniform(0.9, 1.5))

def ifUpgrade():
    pull_screenshot()
    img_rgb = cv2.imread('1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('star.jpg',0)
    w, h = template.shape[::-1]
 
    method = cv2.TM_CCOEFF_NORMED

# resource
    res = cv2.matchTemplate(img_gray,template,method)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

    threshold = 0.9
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return True
    return False

def getCase():
    img_rgb = cv2.imread('1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('cancelCart.jpg',0)
    w, h = template.shape[::-1]
 
    method = cv2.TM_CCOEFF_NORMED

# resource
    res = cv2.matchTemplate(img_gray,template,method)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.CHOCOLATE
# battle task
    template = cv2.imread('sure.jpg',0)
    w, h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED


    res = cv2.matchTemplate(img_gray,template,method)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.VANILLA

#  battle
    template = cv2.imread('attack.jpg',0)
    w, h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED

    res = cv2.matchTemplate(img_gray,template,method)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.BERRY
# city
    template = cv2.imread('backArrow.jpg',0)
    w, h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED

    res = cv2.matchTemplate(img_gray,template,method)
    threshold = 0.9
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.PEACH

    return TaskType.NONE

def press_sure():
    print("press sure")
    s.tap(420, 200+45)
    time.sleep(random.uniform(0.9, 1.5))

def press_attack():
    print("press combat attack")
    s.tap(420, 330)
    time.sleep(random.uniform(7, 9))
    print("press combat plan")
    s.tap(600, 30) # choose plan
    time.sleep(random.uniform(0.9, 1.5))

    print("press combat plan 6")
    s.tap(650, 200) #plan 6
    time.sleep(random.uniform(0.9, 1.5))

    print("press heal hero")
    s.tap(420, 200+45)
    s.tap(420, 200+45)
    s.tap(420, 200+45)
    s.tap(420, 200+45)
    time.sleep(random.uniform(0.9, 1.5))

    print("press combat attacking")
    s.tap(650, 390) #start
    time.sleep(random.uniform(45, 50))
    print("press combat attacking complete")
    s.tap(500, 390) #finish
    time.sleep(random.uniform(3, 4))

    # if ifUpgrade():
    #     print("press combat hero upgrade")
    #     s.tap(400, 390) #finish
    #     time.sleep(random.uniform(3, 4))

    print("press combat hero exp")
    s.tap(400, 390) #finish
    time.sleep(random.uniform(3, 4))
    print("press combat loot")
    s.tap(400, 390) #finish
    time.sleep(random.uniform(0.9, 1.5))

def press_combat():
    print("press combat start")
    s.tap(420, 200+45) #sure
    time.sleep(random.uniform(0.9, 1.5))
    press_attack()

class TaskType(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    BERRY = 3
    PEACH = 4
    NONE = 5

#380, 200
def main():
    count = 0
    success = 0
    fail = 0
    tryNext = 1
    pull_screenshot()
    
    while True:
        count += 1
        press_quest()
        #press_rank()
        go_to_quest(tryNext)

        func_set = press_up_left
        time.sleep(random.uniform(1, 2))
        if fail == 0:
            time.sleep(random.uniform(79, 88))
        elif fail == 1:
            func_set = press_up_right
        elif fail == 2:
            func_set = press_down_right
        elif fail == 3:
            func_set = press_down_left  
        elif fail == 4:
            func_set = press_up
        elif fail == 5:
            func_set = press_down
        elif fail == 6:
            func_set = press_left
        elif fail == 7:
            func_set = press_right
        elif fail == 8:
            fail = 0
            func_set = press_up_left

        func_set()
        time.sleep(random.uniform(3, 4))
        pull_screenshot()
        ttype = getCase()

        if ttype == TaskType.CHOCOLATE:
            press_sure()
            fail = 0
            success += 1
            print("sucess = " ,success, success*100/count)
        elif ttype == TaskType.VANILLA:
            press_combat()
            fail = 0
            success += 1
            print("sucess = " ,success, success*100/count)
        elif ttype == TaskType.BERRY:
            press_attack()
            print("do small task")
            fail += 1
        elif ttype == TaskType.PEACH:
            press_back()
            print("went to city, BACK!")
            fail += 1
        else:
            print("can not find")
            fail += 1
            

if __name__ == '__main__':
    main()
