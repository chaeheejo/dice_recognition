import cv2 as cv

img = cv.imread('broad_side_image/1.png')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,200,255, cv.THRESH_BINARY_INV)
edge = cv.Canny(thresh,9, 150)

cv.imshow('edge', edge)
cv.waitKey()

circles = cv.HoughCircles(edge,cv.HOUGH_GRADIENT,1.2,29,param1=50,param2=14,minRadius=24,maxRadius=35)

circles=circles[0,:]

#show detected dice at image
for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('img', rgb_img)
cv.waitKey()

print('#1 dice value is', len(circles))



img = cv.imread('broad_side_image/2.png')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,170,255, cv.THRESH_BINARY_INV)
edge = cv.Canny(thresh,9, 150)

cv.imshow('edge2', edge)
cv.waitKey()

circles = cv.HoughCircles(edge,cv.HOUGH_GRADIENT,1.2,29,param1=50,param2=14,minRadius=24,maxRadius=35)

circles=circles[0,:]

#show detected dice at image
for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('img', rgb_img)
cv.waitKey()

print('#2 dice value is', len(circles))

