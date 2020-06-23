import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

def HSItoRGB(img):

    H = img[:, :, 0]*(math.pi/180)
    S = img[:, :, 1]/100
    I = img[:, :, 2]/255

    func = np.vectorize(math.cos)
    x = I * (1 - S)
    y = I*(1 + ((S*func(H)) / (func((math.pi/3) - H))))
    z = 3*I - (x + y)

    res = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if H[i][j] < 2*math.pi/3:
                res[:, :, 2] = x
                res[:, :, 0] = y
                res[:, :, 1] = z
            elif H[i][j] < 4*math.pi/3 and H >= 2*math.pi/3:
                res[:, :, 0] = x
                res[:, :, 1] = y
                res[:, :, 2] = z
            else:
                res[:, :, 1] = x
                res[:, :, 2] = y
                res[:, :, 0] = z

    res = res*255
    res = res.astype(np.uint8)
    return res

def RGBtoHSI(img):
    img = img / 255
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    num = 0.5*((r - g) + (r - b))
    den = (((r - g)**2) + ((r - b)*(g - b)))**0.5
    func = np.vectorize(math.cos)
    H = func(num/(den + 0.0000001))
    H[b > g] = (2*math.pi) - H[b > g]
    H = H*(180/math.pi)
    # print(H)

    S = np.zeros(img[:, :, 0].shape)
    for i in range(len(S)):
        for j in range(len(S[0])):
            S[i][j] = 1 - (3 / (r[i][j] + g[i][j] + b[i][j] + 0.0000001))*min(r[i][j], g[i][j], b[i][j])
            S[i][j] = S[i][j]*100

    # print(S)
    # S = 1 - (3. / (r + g + b + 0.000001)).* min(I, [], 3)
    I = (r + g + b)/3
    I = I*255
    res = np.zeros(img.shape)
    res[:, :, 0] = H
    res[:, :, 1] = S
    res[:, :, 2] = I
    # res[:, :, 2] = func2(res[:, :, 2])
    return res

def histogram_equl(img_in):

    print(img_in.shape)
    h, bin = np.histogram(img_in.flatten(), 256, [0, 256])
    cdf = np.cumsum(h)
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')
    img_p = cdf_final[img_in]

    return img_p


img = cv2.imread('InputImages_PracticeSet-6/input1.PNG')
res = img[:, :, :]
# hist,bins = np.histogram(img.flatten(),256,[0,256])
# plt.hist(img.flatten(),256,[0,256], color = 'r')
res[:, :, 0] = histogram_equl(res[:, :, 0])
res[:, :, 1] = histogram_equl(res[:, :, 1])
res[:, :, 2] = histogram_equl(res[:, :, 2])
cv2.imwrite('result.jpg', res)
# cv2.waitKey(0)
# plt.xlim([0,256])
# plt.show()

# RGB to HSI
HSI = RGBtoHSI(img)
HSI = HSI.astype(np.uint8)
cv2.imwrite('HSI.jpg', HSI)
# print(HSI[:, :, 2])
HSI_conv = HSI[:, :, :]
# HSI_conv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
HSI_conv[:, :, 2] = histogram_equl(HSI_conv[:, :, 2])
# RGB = cv2.cvtColor(HSI_conv, cv2.COLOR_HSV2BGR)
RGB = HSItoRGB(HSI_conv)
cv2.imwrite('HSIimage.jpg', RGB)
cv2.waitKey(0)