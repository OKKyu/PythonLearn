#! python3
# -*- coding:utf-8 -*-
import cv2

__wait_time = 2000

#gray scale
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_GRAYSCALE)
#display image
cv2.imshow("IMREAD_GRAYSCALE",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_GRAYSCALE")

#any color
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_ANYCOLOR)
#display image
cv2.imshow("IMREAD_ANYCOLOR",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_ANYCOLOR")

#any depth
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_ANYDEPTH)
#display image
cv2.imshow("IMREAD_ANYDEPTH",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_ANYDEPTH")

#reduce color 2
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_REDUCED_COLOR_2)
#display image
cv2.imshow("IMREAD_REDUCED_COLOR_2",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_REDUCED_COLOR_2")

#reduce color 4
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_REDUCED_COLOR_4)
#display image
cv2.imshow("IMREAD_REDUCED_COLOR_4",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_REDUCED_COLOR_4")

#reduce color 8
img = cv2.imread('/home/puppy/pic/UriHamushi.jpg', cv2.IMREAD_REDUCED_COLOR_8)
#display image
cv2.imshow("IMREAD_REDUCED_COLOR_8",img)
cv2.waitKey(__wait_time)
cv2.destroyWindow("IMREAD_REDUCED_COLOR_8")

cv2.destroyAllWindows()