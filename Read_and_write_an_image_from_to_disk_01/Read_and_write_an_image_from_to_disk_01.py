import numpy as np
import cv2
 
img = cv2.imread("images_to_test_scripts/opencv-logo.png")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.imwrite("images_to_test_scripts/output.jpg",img)
