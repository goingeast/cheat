import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt


img_rgb = cv2.imread('buguan.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('buguanta.jpg',0)
w, h = template.shape[::-1]
 
method = cv2.TM_CCOEFF_NORMED

# Apply template Matching
res = cv2.matchTemplate(img_gray,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png', img_rgb)