import cv2
import os
from matplotlib import pyplot as plt

list_image = os.listdir('Test/NG')
for file in list_image:
    img = cv2.imread('Test/NG/' + file)
    img_1 = img[200:2830, 800:2400]
    img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

    histr = cv2.calcHist([img_1], [0], None, [256], [0, 256])
    plt.subplot(121)
    plt.imshow(img_1)
    plt.subplot(122)
    plt.plot(histr)
    plt.show()

    mask_1 = img_1[870:980, 1130:1590]
    # mask_2 = img_1[870:1640, 1490:1590]
    mask_3 = img_1[1510:1640, 1130:1590]
    mask_4 = img_1[930:1460, 0:135]
    mask_5 = img_1[2310:2620, 270:390]
    mask_6 = img_1[2310:2620, 890:1000]

    histr_1 = cv2.calcHist([mask_1], [0], None, [256], [0, 256])
    # histr_2 = cv2.calcHist([mask_2], [0], None, [256], [0, 256])
    histr_3 = cv2.calcHist([mask_3], [0], None, [256], [0, 256])
    histr_4 = cv2.calcHist([mask_4], [0], None, [256], [0, 256])
    histr_5 = cv2.calcHist([mask_5], [0], None, [256], [0, 256])
    histr_6 = cv2.calcHist([mask_6], [0], None, [256], [0, 256])

    plt.subplot(421)
    plt.imshow(mask_1)
    plt.subplot(422)
    plt.plot(histr_1)
    plt.subplot(423)
    plt.imshow(mask_3)
    plt.subplot(424)
    plt.plot(histr_3)
    plt.subplot(425)
    plt.imshow(mask_4)
    plt.subplot(426)
    plt.plot(histr_4)
    plt.subplot(427)
    plt.imshow(mask_5)
    plt.subplot(428)
    plt.plot(histr_5)
    plt.show()