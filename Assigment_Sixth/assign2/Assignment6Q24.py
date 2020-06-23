import cv2
import numpy as np

image = cv2.imread('Input images/hw2_4.tif', 0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 500
params.maxArea = 2000

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of small Blobs in red color: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()