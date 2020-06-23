import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

def apply_brightness_contrast(hsv, intensity_change, saturation_change):
    hsv[:, :, 2] = hsv[:, :, 2] + intensity_change
    hsv[:, :, 1] = hsv[:, :, 1] + saturation_change

    return hsv

def funcBrightContrast(bright=0):
    bright = cv2.getTrackbarPos('intensity', 'Trackbar')
    contrast = cv2.getTrackbarPos('saturation', 'Trackbar')
    print(bright, contrast)
    effect = apply_brightness_contrast(hsv, bright, contrast)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('Effect',img)

if __name__ == "__main__":
    img = cv2.imread("lena.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.namedWindow('Trackbar', 1)
    int_max = 0
    sat_max = 0
    Set_I = set()
    Set_S = set()
    for x in range(0, len(hsv)):
        for y in range(0, len(hsv[0])):
            int_max = max(int_max, hsv[x, y][2])
            sat_max = max(sat_max, hsv[x, y][1])
            Set_I.add(hsv[x, y][2])
            Set_S.add(hsv[x, y][1])

    intensity = hsv[0, 0, 2]
    saturation = hsv[0, 0, 1]

    print(Set_S)
    print(Set_I)
    cv2.createTrackbar('intensity', 'Trackbar', 0, 2 * int_max, funcBrightContrast)
    cv2.createTrackbar('saturation', 'Trackbar', 0, 2 * sat_max, funcBrightContrast)
    funcBrightContrast(0)




# print(hsv[:,:,2])
# for x in range(0, len(hsv)):
#     for y in range(0, len(hsv[0])):
#         if hsv[x, y][2] < 0:
#             print(hsv[x, y][2])
#             hsv[x, y][2] = 0

# img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# cv2.imshow('HSV Image',img)
cv2.waitKey(0)