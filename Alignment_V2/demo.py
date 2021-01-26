import cv2
import os
from matplotlib import pyplot as plt

class Alignment(object):
    def __init__(self):

    def check_mask_down(self):
        mask_left_1 = raw[260:530, 250:310]
        mask_left_2 = raw[800:1590, 160:220]
        mask_left_3 = raw[1750:1970, 200:260]
        mask_left_4 = raw[1640:1800, 265:330]
    def check_mask_up(self):

    def check_mask_left(self):
    
    def check_mask_right(self):

    def plot(self):
list_image = os.listdir('Test/NG')
for file in list_image:
    img = cv2.imread('Test/NG/' + file)
    raw = img[200:2830, 800:2400]
    raw = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)

    histr_raw = cv2.calcHist([raw], [0], None, [256], [0, 256])
    plt.subplot(121)
    plt.imshow(raw)
    plt.subplot(122)
    plt.plot(histr_raw)
    plt.show()

    mask = [[list] * 10]
    histr = [[list] * 10]

    mask[0] = raw[260:530, 250:310]
    mask[1] = raw[800:1590, 160:220]
    mask[2] = raw[1750:1970, 200:260]
    mask[3] = raw[1640:1800, 265:330]
    mask[4] = raw[1920:2190, 280:325]
    mask[5] = raw[2170:2225, 280:825]
    mask[6] = raw[2235:2295, 685:985]
    mask[7] = raw[1635:2300, 955:990]
    mask[8] = raw[800:1600, 1060:1110]
    mask[9] = raw[60:200, 795:975]

    histr[0] = cv2.calcHist([mask[0]], [0], None, [256], [0, 256])
    histr[1] = cv2.calcHist([mask[1]], [0], None, [256], [0, 256])
    histr[2] = cv2.calcHist([mask[2]], [0], None, [256], [0, 256])
    histr[3] = cv2.calcHist([mask[3]], [0], None, [256], [0, 256])
    histr[4] = cv2.calcHist([mask[4]], [0], None, [256], [0, 256])
    histr[5] = cv2.calcHist([mask[5]], [0], None, [256], [0, 256])
    histr[6] = cv2.calcHist([mask[6]], [0], None, [256], [0, 256])
    histr[7] = cv2.calcHist([mask[7]], [0], None, [256], [0, 256])
    histr[8] = cv2.calcHist([mask[8]], [0], None, [256], [0, 256])
    histr[9] = cv2.calcHist([mask[9]], [0], None, [256], [0, 256])

    if histr[:][80:120].any() > 100:
        print("NG")

    # plt.subplot(421)
    # plt.imshow(mask_1)
    plt.subplot(421)
    plt.plot(histr[0])
    # plt.subplot(422)
    # plt.imshow(mask_2)
    plt.subplot(422)
    plt.plot(histr[1])
    # plt.subplot(423)
    # plt.imshow(mask_3)
    plt.subplot(423)
    plt.plot(histr[2])
    # plt.subplot(424)
    # plt.imshow(mask_4)
    plt.subplot(424)
    plt.plot(histr[3])
    # plt.subplot(425)
    # plt.imshow(mask_5)
    plt.subplot(425)
    plt.plot(histr[4])
    # plt.subplot(426)
    # plt.imshow(mask_6)
    plt.subplot(426)
    plt.plot(histr[5])
    # plt.subplot(427)
    # plt.imshow(mask_7)
    plt.subplot(427)
    plt.plot(histr[6])
    # plt.subplot(428)
    # plt.imshow(mask_8)
    plt.subplot(428)
    plt.plot(histr[7])

    plt.show()