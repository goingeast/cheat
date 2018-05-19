# -*- coding: utf-8 -*-
import os
import shutil
import time
import math
import random
import json
from PIL import Image, ImageDraw
from enum import Enum
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt

from common import screenshot
from common.auto_adb import auto_adb

VERSION = "0.0.1"

screenshot_backup_dir = 'screenshot_backups/'

adb = auto_adb()

keypoint = {'quest':[100,1070 - 100],
            'quest1':[1300, 1070 - 800],
            'quest2':[1300, 1070 - 800 + 210],
            'back':[50,50],
            'go':[1020,1070 - 420],
            'move-up-left':[960 -100 *1.2, 1070 - 590 - 100 *1.2],
            'move-up-right':[960 +100*1.2, 1070 - 590 - 100*1.2],
            'move-down-left':[960 -100*1.3, 1070 - 590 + 100*1.3],
            'move-down-right':[960 +100*1.3, 1070 - 590 + 100*1.3],
            'move-up':[960 , 1070 - 590 - 120*1.1],
            'move-down':[960 , 1070 - 590 + 120*1.1],
            'move-left':[960 -120*1.1, 1070 - 590],
            'move-right':[960 +120*1.1, 1070 - 590],
            'sure':[1020,1070-400],
            'attack':[1200, 1070 -250],
            'plans':[1600, 1070 - 970],
            'plan6':[1750, 1070 - 570],
            'recover':[1200, 1070 -350],
            'start':[1750, 1070 - 160],
            'complete':[1200, 1070 - 100],
            'heroexp':[1000, 1070 - 100],
            'loot':[1000, 1070 -200]}


def tap(x , y):
    cmd = 'shell input tap {x1} {y2}'.format(
        x1=x,
        y2=y,
    )
    print(cmd)
    adb.run(cmd)

if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)


def pull_screenshot():
    screenshot.pull_screenshot()


def press_quest():
    print("Quest button pressed")
    tap(keypoint['quest'][0], keypoint['quest'][1])
    time.sleep(random.uniform(0.9, 1.5))
    #tap(30,30)
    #time.sleep(random.uniform(0.9, 1.5))
   # tap(80, 360)
def press_back():
    print("Back button pressed")
    tap(keypoint['back'][0], keypoint['back'][1])
    time.sleep(random.uniform(0.5, 1.0))

def go_to_quest(number):
    print("Go to Quest button pressed")
    tap(keypoint['quest2'][0], keypoint['quest2'][1])
    time.sleep(random.uniform(0.9, 1.5))
    tap(keypoint['go'][0], keypoint['go'][1])
    

def press_rank():
    print("Map button pressed")
    tap(500, 390)
    time.sleep(random.uniform(0.9, 1.5))
    tap(30,30)
    time.sleep(random.uniform(0.9, 1.5))

def press_map():
    print("Map button pressed")
    tap(120, 390)
    time.sleep(random.uniform(0.9, 1.5))
    tap(30,30)
    time.sleep(random.uniform(0.9, 1.5))

def press_home():
    print("Home button pressed")
    tap(200, 390)
    time.sleep(random.uniform(0.9, 1.5))
    tap(30,30)
    time.sleep(random.uniform(0.9, 1.5))

def press_up_left():
    print("up left pressed")
    tap(keypoint['move-up-left'][0], keypoint['move-up-left'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_up_right():
    print("up right pressed")
    tap(keypoint['move-up-right'][0], keypoint['move-up-right'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_down_left():
    print("down left  pressed")
    tap(keypoint['move-down-left'][0], keypoint['move-down-left'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_down_right():
    print("down right pressed")
    tap(keypoint['move-down-right'][0], keypoint['move-down-right'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_up():
    print("up pressed")
    tap(keypoint['move-up'][0], keypoint['move-up'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_down():
    print("down pressed")
    tap(keypoint['move-down'][0], keypoint['move-down'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_left():
    print("left pressed")
    tap(keypoint['move-left'][0], keypoint['move-left'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_right():
    print("right pressed")
    tap(keypoint['move-right'][0], keypoint['move-right'][1])
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

    template = cv2.imread('cancelCart_a.jpg',0)
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
    template = cv2.imread('sure_a.jpg',0)
    w, h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED


    res = cv2.matchTemplate(img_gray,template,method)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.VANILLA

#  battle
    template = cv2.imread('attack_a.jpg',0)
    w, h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED

    res = cv2.matchTemplate(img_gray,template,method)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        return TaskType.BERRY
# city
    template = cv2.imread('backArrow_a.jpg',0)
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
    tap(keypoint['sure'][0], keypoint['sure'][1])
    time.sleep(random.uniform(0.9, 1.5))

def press_attack():
    print("press combat attack")
    tap(keypoint['attack'][0], keypoint['attack'][1])
    time.sleep(random.uniform(7, 9))
    print("press combat plan")
    tap(keypoint['plans'][0], keypoint['plans'][1]) # choose plan
    time.sleep(random.uniform(0.9, 1.5))

    print("press combat plan 6")
    tap(keypoint['plan6'][0], keypoint['plan6'][1]) #plan 6
    time.sleep(random.uniform(0.9, 1.5))

    print("press heal hero")
    tap(keypoint['recover'][0], keypoint['recover'][1])
    tap(keypoint['recover'][0], keypoint['recover'][1])
    tap(keypoint['recover'][0], keypoint['recover'][1])
    tap(keypoint['recover'][0], keypoint['recover'][1])

    time.sleep(random.uniform(0.9, 1.5))

    print("press combat attacking")
    tap(keypoint['start'][0], keypoint['start'][1]) #start
    time.sleep(random.uniform(45, 50))
    print("press combat attacking complete")
    tap(keypoint['complete'][0], keypoint['complete'][1]) #finish
    time.sleep(random.uniform(3, 4))

    # if ifUpgrade():
    #     print("press combat hero upgrade")
    #     tap(400, 390) #finish
    #     time.sleep(random.uniform(3, 4))

    print("press combat hero exp")
    tap(keypoint['heroexp'][0], keypoint['heroexp'][1]) #finish
    time.sleep(random.uniform(3, 4))
    print("press combat loot")
    tap(keypoint['loot'][0], keypoint['loot'][1]) #finish
    time.sleep(random.uniform(0.9, 1.5))

def press_combat():
    print("press combat start")
    press_sure()
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
