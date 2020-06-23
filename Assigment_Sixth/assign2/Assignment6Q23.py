import cv2
import numpy as np
import matplotlib.pyplot as plt

def backgroundRemoval(image, num_of_rows, num_of_cols):
    final_background_removed_image = np.zeros([num_of_rows, num_of_cols], image[0][0])

    # histogram_array = [0 for i in range(256)]
    # bin_edges = [i for i in range(256)]

    for x in range(num_of_rows):
        minimum_value = image[x][0]

        for y in range(1, num_of_cols):
            if image[x][y] < minimum_value:
                minimum_value = image[x][y]

        for y in range(num_of_cols):
            final_background_removed_image[x][y] = image[x][y] - minimum_value
            # histogram_array[final_background_removed_image[x][y]] += 1

    for x in range(num_of_rows):
        for y in range(num_of_cols):
            if final_background_removed_image[x][y] < 66:           # threshold value was decided using histogram analysis
                final_background_removed_image[x][y] = 0

    cv2.imshow("Orignal Image", image)
    cv2.imshow("Final Image", final_background_removed_image)
    cv2.waitKey(0)

    # plt.title("Histogram")
    # plt.bar(bin_edges, histogram_array, width=0.3)
    # plt.xlabel("GrayScale Values")
    # plt.ylabel("Number of pixels")
    # plt.plot(bin_edges, histogram_array, 'G')
    # plt.show()

def main():
    image = cv2.imread("Input images/hw2_3.tif", 0)

    num_of_rows = image.shape[0]
    num_of_cols = image.shape[1]

    backgroundRemoval(image, num_of_rows, num_of_cols)

main()