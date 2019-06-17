#! python3
# -*- coding:utf-8 -*-
import cv2

#read image
img = cv2.imread('/home/puppy/pic/pillowBasic001.jpg', cv2.IMREAD_COLOR)
#display image
cv2.imshow("image",img)
cv2.waitKey(0)

#overwriting image to existed window
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.waitKey(0)

#open many windows
cv2.imshow("image2",img)
cv2.imshow("image3",img)
#wait 5 seconds and close one windo
cv2.waitKey(5000)
cv2.destroyWindow("image3")
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()