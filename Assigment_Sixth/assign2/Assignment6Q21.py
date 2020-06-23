import cv2
import numpy as np

def erosion(image, num_of_rows, num_of_cols):
    structure_element = np.zeros([3, 1], image[0][0])
    eroded_image = np.zeros([num_of_rows, num_of_cols], image[0][0])
    eroded_image2 = np.zeros([num_of_rows, num_of_cols], image[0][0])
    eroded_image3 = np.zeros([num_of_rows, num_of_cols], image[0][0])


    # print(image[200][200] + np.sum(structure_element))
    # print(np.subtract(image[200:203, 200:201], structure_element))
    for x in range(num_of_rows-2):
        for y in range(num_of_cols):
            # sum_of_pixels = np.sum(structure_element) + np.sum(image[x:x+3, y:y+1])
            subtracted_array = np.subtract(image[x:x+3, y:y+1], structure_element)
            eroded_image[x+1][y] = np.amin(subtracted_array)

    for x in range(num_of_rows-2):
        for y in range(num_of_cols):
            # sum_of_pixels = np.sum(structure_element) + np.sum(image[x:x+3, y:y+1])
            subtracted_array = np.subtract(eroded_image[x:x+3, y:y+1], structure_element)
            eroded_image2[x + 1][y] = np.amin(subtracted_array)

    for x in range(num_of_rows-2):
        for y in range(num_of_cols):
            # sum_of_pixels = np.sum(structure_element) + np.sum(image[x:x+3, y:y+1])
            subtracted_array = np.subtract(eroded_image2[x:x+3, y:y+1], structure_element)
            eroded_image3[x + 1][y] = np.amin(subtracted_array)


    cv2.imshow("Original Image", image)
    # cv2.imshow("Eroded Image", eroded_image)
    # cv2.imshow("Eroded Image 2", eroded_image2)
    cv2.imshow("Image after three erosions", eroded_image3)
    cv2.waitKey(0)


def main():
    image = cv2.imread("Input images/hw2_1.tif", 0)


    num_of_rows = image.shape[0]
    num_of_cols = image.shape[1]
    # print(image_matrix)

    erosion(image, num_of_rows, num_of_cols)


    # print(num_of_rows)
    # print(num_of_cols)
main()

