import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

color_image = cv2.imread("lena.png")

# cv2.imshow("Original Image", color_image)
# cv2.waitKey(0)

num_of_rows = color_image.shape[0]
num_of_cols = color_image.shape[1]

NORMALIZED_image_array = np.zeros([num_of_rows, num_of_cols], dtype='d, d, d')
IHS_array = np.zeros([num_of_rows, num_of_cols], dtype='d, d, d')

# print(color_image.shape)
# print(color_image[200][200])

bin_edges = [i for i in range(256)]
red_color_array = [0 for i in range(256)]
green_color_array = [0 for i in range(256)]
blue_color_array = [0 for i in range(256)]

intensity_array = [0 for i in range(256)]

for x in range(num_of_rows):
    for y in range(num_of_cols):
        red_color_array[color_image[x][y][0]] += 1
        green_color_array[color_image[x][y][1]] += 1
        blue_color_array[color_image[x][y][2]] += 1

for x in range(num_of_rows):
    for y in range(num_of_cols):
        NORMALIZED_image_array[x][y][0] = color_image[x][y][0]/(color_image[x][y][0] + color_image[x][y][1] + color_image[x][y][2])
        NORMALIZED_image_array[x][y][1] = color_image[x][y][1]/(color_image[x][y][0] + color_image[x][y][1] + color_image[x][y][2])
        NORMALIZED_image_array[x][y][2] = color_image[x][y][2]/(color_image[x][y][0] + color_image[x][y][1] + color_image[x][y][2])

for x in range(num_of_rows):
    for y in range(num_of_cols):
        RED_component = NORMALIZED_image_array[x][y][0]
        GREEN_component = NORMALIZED_image_array[x][y][1]
        BLUE_component = NORMALIZED_image_array[x][y][2]

        if RED_component == GREEN_component and GREEN_component == BLUE_component:
            IHS_array[x][y][0] = (RED_component + GREEN_component + BLUE_component)/3
        else:
            IHS_array[x][y][0] = (RED_component + GREEN_component + BLUE_component)/3

            theta = math.acos((0.5 * (2*RED_component - GREEN_component - BLUE_component))/math.sqrt(math.pow(RED_component-GREEN_component, 2) + (RED_component-BLUE_component)*(GREEN_component-BLUE_component)))

            if BLUE_component <= GREEN_component:
                IHS_array[x][y][1] = theta
            else:
                IHS_array[x][y][1] = 360 - theta

            IHS_array[x][y][2] = 1 - (3 * min(RED_component, GREEN_component, BLUE_component))/(RED_component + GREEN_component + BLUE_component)



# print(red_color_array)
# print(green_color_array)
# print(blue_color_array)

plt.title("Statistics for Red Color")
plt.xlabel("Values")
plt.ylabel("No. of values")
plt.plot(bin_edges, red_color_array, 'R')
# plt.plot(bin_edges, green_color_array, 'G')
# plt.plot(bin_edges, blue_color_array, 'B')
plt.show()

plt.title("Statistics for Green Color")
plt.xlabel("Values")
plt.ylabel("No. of values")
plt.plot(bin_edges, green_color_array, 'G')
plt.show()

plt.title("Statistics for Blue Color")
plt.xlabel("Values")
plt.ylabel("No. of values")
plt.plot(bin_edges, blue_color_array, 'B')
plt.show()

print("The Normalized RGB Array is:-\n", NORMALIZED_image_array)
print("IHS components of each pixel:-\n", IHS_array)


