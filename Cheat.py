# -*- coding: utf-8 -*-
import os
import shutil
import time
import math
import random
import json
from PIL import Image, ImageDraw
import wda


with open('config.json', 'r') as f:
    config = json.load(f)

VERSION = "0.0.1"
c = wda.Client()
s = c.session()

screenshot_backup_dir = 'screenshot_backups/'

if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)


def pull_screenshot():
    c.screenshot('1.png')


def jump(distance):
    press_time = 1000
    print('press time: {}'.format(press_time))
    s.tap_hold(random.uniform(0, 320), random.uniform(64, 320), press_time)

def press_map():
    print("Map button pressed")
    c.tap(10, 10)

def main():
    while True:
        pull_screenshot()
        im = Image.open("./1.png")

        press_map()


if __name__ == '__main__':
    main()
