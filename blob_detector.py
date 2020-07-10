# Standard imports
import cv2
import numpy as np;
# Read image
im = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
print("im is:",im)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
print("detector is:",detector)
# Detect blobs.
keypoints = detector.detect(im)
print("keypoints are:",keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print("im_with_keypoints are:",im_with_keypoints)
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)


