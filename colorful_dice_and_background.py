import cv2 as cv

img = cv.imread('colorful_dice_and_background_image/1.jpg')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,220,255, cv.THRESH_BINARY_INV)
edge = cv.Canny(thresh, 9, 150)

contours, hierarchy = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

x0, y0, w0, h0= cv.boundingRect(contours[0])
x1, y1, w1, h1= cv.boundingRect(contours[1])

first_dice = edge[y0:y0 + h0, x0:x0 + w0]
second_dice = edge[y1:y1 + h1, x1:x1 + w1]

first_circles = cv.HoughCircles(first_dice,cv.HOUGH_GRADIENT,1.2,20,param1=50,param2=25,minRadius=3,maxRadius=35)
second_circles = cv.HoughCircles(second_dice,cv.HOUGH_GRADIENT,1.2,20,param1=50,param2=25,minRadius=3,maxRadius=35)
print('#1 In ascending order, the dice value is', len(first_circles[0]), len(second_circles[0]))

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



img = cv.imread('several_colorful_dice_background_image/2.jpg')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,220,255, cv.THRESH_BINARY_INV)

edge_ = cv.Canny(thresh,9, 150)
dilate = cv.dilate(edge_, None)

contours, hierarchy = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

x0, y0, w0, h0= cv.boundingRect(contours[0])
x1, y1, w1, h1= cv.boundingRect(contours[1])
x2, y2, w2, h2= cv.boundingRect(contours[2])

first_dice_ = edge_[y0:y0+h0, x0:x0+w0]
second_dice_ = edge_[y1:y1+h1, x1:x1+w1]
third_dice_ = edge_[y2:y2+h2, x2:x2+w2]

first_circles_ = cv.HoughCircles(first_dice_,cv.HOUGH_GRADIENT,1.2,30,param1=50,param2=30,minRadius=20,maxRadius=35)
second_circles_ = cv.HoughCircles(second_dice_,cv.HOUGH_GRADIENT,1.2,30,param1=50,param2=30,minRadius=20,maxRadius=35)
third_circles_ = cv.HoughCircles(third_dice_,cv.HOUGH_GRADIENT,1.2,30,param1=50,param2=30,minRadius=20,maxRadius=35)

sorted_circles = sorted([len(first_circles_[0]), len(second_circles_[0]), len(third_circles_[0])])
print('#2 In ascending order, the dice value is', sorted_circles[0], sorted_circles[1], sorted_circles[2])

#show detected dice at image
cv.rectangle(rgb_img, (x0,y0),(x0+w0,y0+h0), (255,0,0),5)
cv.rectangle(rgb_img, (x1,y1),(x1+w1,y1+h1), (255,0,0),5)
cv.rectangle(rgb_img, (x2,y2),(x2+w2,y2+h2), (255,0,0),5)

circles = cv.HoughCircles(edge_,cv.HOUGH_GRADIENT,1.2,30,param1=50,param2=30,minRadius=20,maxRadius=35)
circles=circles[0,:]

for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('rgb_img', rgb_img)
cv.waitKey()



img = cv.imread('several_colorful_dice_background_image/3.png')
rgb_img = img[:]
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(img,220,255, cv.THRESH_BINARY_INV)
edge__ = cv.Canny(thresh,9, 150)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
dilate = cv.dilate(edge__,kernel,iterations = 1)

contours, hierarchy = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

x0, y0, w0, h0= cv.boundingRect(contours[0])
x1, y1, w1, h1= cv.boundingRect(contours[1])
x2, y2, w2, h2= cv.boundingRect(contours[2])
x3, y3, w3, h3= cv.boundingRect(contours[3])
x4, y4, w4, h4= cv.boundingRect(contours[4])
x5, y5, w5, h5= cv.boundingRect(contours[5])

first_dice__ = edge__[y0:y0+h0, x0:x0+w0]
second_dice__ = edge__[y1:y1+h1, x1:x1+w1]
third_dice__ = edge__[y2:y2+h2, x2:x2+w2]
fourth_dice__ = edge__[y3:y3+h3, x3:x3+w3]
fifth_dice__ = edge__[y4:y4+h4, x4:x4+w4]
sixth_dice__ = edge__[y5:y5+h5, x5:x5+w5]

first_circles__ = cv.HoughCircles(first_dice__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)
second_circles__ = cv.HoughCircles(second_dice__,cv.HOUGH_GRADIENT,1.2,80,param1=50,param2=30,minRadius=10,maxRadius=35)
third_circles__ = cv.HoughCircles(third_dice__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)
fourth_circles__ = cv.HoughCircles(fourth_dice__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)
fifth_circles__ = cv.HoughCircles(fifth_dice__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)
sixth_circles__ = cv.HoughCircles(sixth_dice__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)

sorted_circles = sorted([len(first_circles__[0]), len(second_circles__[0]), len(third_circles__[0]), len(fourth_circles__[0]),
                         len(fifth_circles__[0]), len(sixth_circles__[0])])
print('#3 In ascending order, the dice value is', sorted_circles[0], sorted_circles[1], sorted_circles[2], sorted_circles[3], sorted_circles[4],
      sorted_circles[5])

#show detected dice at image
cv.rectangle(rgb_img, (x0,y0),(x0+w0,y0+h0), (255,0,0),5)
cv.rectangle(rgb_img, (x1,y1),(x1+w1,y1+h1), (255,0,0),5)
cv.rectangle(rgb_img, (x2,y2),(x2+w2,y2+h2), (255,0,0),5)
cv.rectangle(rgb_img, (x3,y3),(x3+w3,y3+h3), (255,0,0),5)
cv.rectangle(rgb_img, (x4,y4),(x4+w4,y4+h4), (255,0,0),5)
cv.rectangle(rgb_img, (x5,y5),(x5+w5,y5+h5), (255,0,0),5)

circles = cv.HoughCircles(edge__,cv.HOUGH_GRADIENT,1.2,60,param1=50,param2=30,minRadius=10,maxRadius=35)
circles=circles[0,:]

for circle in circles:
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),int(circle[2]),(255,0,0),2)
    cv.circle(rgb_img,(int(circle[0]),int(circle[1])),2,(0,0,255),3)

cv.imshow('rgb_img', rgb_img)
cv.waitKey()