import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

intensity_change = int(input("Type the value you want to change the intensity by: "))
saturation_change = int(input("Type the value you want to change the saturation by: "))

img = cv2.imread("lena.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv[:,:,2] = hsv[:,:,2] + intensity_change
hsv[:,:,1] = hsv[:,:,1] + saturation_change
# print(hsv[:,:,2])
# for x in range(0, len(hsv)):
#     for y in range(0, len(hsv[0])):
#         if hsv[x, y][2] < 0:
#             print(hsv[x, y][2])
#             hsv[x, y][2] = 0

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV Image',img)
cv2.waitKey(0)