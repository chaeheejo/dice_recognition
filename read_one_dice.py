import math
import cv2 as cv

for k in range(4):
    file_path = 'read_one_dice_image/'+str(k+1)+'.png'
    img = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
    _, img_bin = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(img_bin, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cnt=0
    rec=0
    for i in range(len(contours)):
        approx = cv.approxPolyDP(contours[i], cv.arcLength(contours[i], True)*0.02, True)
        parent = hierarchy[0][i][-1]

        if len(approx)==4:
            rec = i
        elif len(approx)>4 and parent==rec :
            length = cv.arcLength(contours[i], True)
            area = cv.contourArea(contours[i])
            ratio = 4.*math.pi*area / (length*length)

            if ratio >0.85 :
                cnt+=1

    print('#%d dice value is' %(k+1), cnt)