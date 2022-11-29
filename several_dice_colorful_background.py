import cv2 as cv

img = cv.imread('several_dice_colorful_background_image/1.jpg')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,150,255, cv.THRESH_BINARY_INV)
edge = cv.Canny(thresh,9, 150)

contours, hierarchy = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

x0, y0, w0, h0= cv.boundingRect(contours[0])
x1, y1, w1, h1= cv.boundingRect(contours[1])

first_dice = edge[y0:y0+h0, x0:x0+w0]
second_dice = edge[y1:y1+h1, x1:x1+w1]

first_circles = cv.HoughCircles(first_dice,cv.HOUGH_GRADIENT,1.2,20,param1=50,param2=25,minRadius=3,maxRadius=35)
second_circles = cv.HoughCircles(second_dice,cv.HOUGH_GRADIENT,1.2,20,param1=50,param2=25,minRadius=3,maxRadius=35)

sorted_circles = sorted([len(first_circles[0]), len(second_circles[0])])
print('#1 In ascending order, the dice value is', sorted_circles[0], sorted_circles[1])

#show detected dice at image
cv.rectangle(rgb_img, (x0,y0),(x0+w0,y0+h0), (255,0,0),5)
cv.rectangle(rgb_img, (x1,y1),(x1+w1,y1+h1), (255,0,0),5)

circles = cv.HoughCircles(edge,cv.HOUGH_GRADIENT,1.2,20,param1=50,param2=25,minRadius=3,maxRadius=35)
circles=circles[0,:]

for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('rgb_img', rgb_img)
cv.waitKey()



img = cv.imread('several_dice_colorful_background_image/2.png')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edge_ = cv.Canny(img, 9, 150)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (9,9))
close = cv.morphologyEx(edge_, cv.MORPH_CLOSE, kernel, iterations=2)

contours, hierarchy = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

x0, y0, w0, h0= cv.boundingRect(contours[2])
x1, y1, w1, h1= cv.boundingRect(contours[3])

first_dice_ = close[y0:y0+h0, x0:x0+w0]
second_dice_ = close[y1:y1+h1, x1:x1+w1]

first_circles_ = cv.HoughCircles(first_dice_,cv.HOUGH_GRADIENT,1.2,50,param1=50,param2=22,minRadius=5,maxRadius=55)
second_circles_ = cv.HoughCircles(second_dice_,cv.HOUGH_GRADIENT,1.2,50,param1=50,param2=22,minRadius=5,maxRadius=55)

sorted_circles = sorted([len(first_circles_[0]), len(second_circles_[0])])
print('#2 In ascending order, the dice value is', sorted_circles[0], sorted_circles[1])

#show detected dice at image
cv.rectangle(rgb_img, (x0,y0),(x0+w0,y0+h0), (255,0,0),5)
cv.rectangle(rgb_img, (x1,y1),(x1+w1,y1+h1), (255,0,0),5)

circles = cv.HoughCircles(close,cv.HOUGH_GRADIENT,1.1,30,param1=50,param2=20,minRadius=5,maxRadius=55)
circles=circles[0,:]

for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('rgb_img', rgb_img)
cv.waitKey()
