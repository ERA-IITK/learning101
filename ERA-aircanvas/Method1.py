import cv2
import numpy as np
import copy
import math
import pygame

#from appscript import app

# Environment:
# OS    : Mac OS EL Capitan
# python: 3.5
# opencv: 2.4.13

# parameters
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8  # start point/total width
threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50
learningRate = 0
pygame.init()
screen=pygame.display.set_mode([1000,100])
running=True
screen.fill((0,0,0))
click=False
pos_prev=None
# variables
isBgCaptured = 0   # bool, whether the background captured
triggerSwitch = False  # if true, keyborad simulator works
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([255,173,127],np.uint8)
def printThreshold(thr):
    print("! Changed threshold to "+str(thr))


def removeBG(frame):
    fgmask = bgModel.apply(frame,learningRate=-1)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((3, 3), np.uint8)
    #fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    imageYCrCb = cv2.cvtColor(res,cv2.COLOR_BGR2YCR_CB)
    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
    fgmask = cv2.bitwise_and(fgmask, fgmask, mask = skinRegion)
    kernel = np.ones((8, 8), np.uint8)
    #fgmask = cv2.equalizeHist(fgmask)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    #gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(fgmask, (5, 5), 0)
    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    return thresh

# Camera
camera = cv2.VideoCapture(0)
camera.set(10,200)
cv2.namedWindow('trackbar')
cv2.createTrackbar('trh1', 'trackbar', threshold, 100, printThreshold)


while camera.isOpened() and running:
    ret, frame = camera.read()
    threshold = cv2.getTrackbarPos('trh1', 'trackbar')
    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    xlimit=frame.shape[1]-cap_region_x_begin * frame.shape[1]
    ylimit=cap_region_y_end * frame.shape[0]
    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                 (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
   # cv2.imshow('original', frame)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #  Main operation
    if isBgCaptured == 1:  # this part wont run until background captured
        imager = frame[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
        #cv2.imshow('mask', img)
        img = removeBG(imager)
        # convert the image into binary image
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
        #cv2.imshow('blur', blur)
        #ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
        #cv2.imshow('ori', thresh)


        # get the coutours
        thresh1 = copy.deepcopy(img)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        maxArea = -1
        if length > 0:
            for i in range(length):  # find the biggest contour (according to area)
                temp = contours[i]
                area = cv2.contourArea(temp)
                if area > maxArea:
                    maxArea = area
                    ci = i
            res = contours[ci]
            hull = cv2.convexHull(res)
            drawing = np.zeros(img.shape, np.uint8)
            cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
            cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)
            m=10000
            pos=0
            for i in range(hull.shape[0]):
                if hull[i][0][1]<m:
                    m=hull[i][0][1]
                    pos=i
            pos_next=tuple(hull[pos][0])
            cv2.circle(drawing, pos_next, 3, (255,255,255), 3)
            cv2.circle(imager, pos_prev, 3, (255,0,0), 3)
            if  pos_prev is not None:       
                if(abs(pos_prev[0]-pos_next[0])<=50 and abs(pos_prev[1]-pos_next[1])<=50):
                    orig=(int(pos_prev[0]*1000/xlimit),int(pos_prev[1]*1000/ylimit))
                    end=(int(pos_next[0]*1000/xlimit),int(pos_next[1]*1000/ylimit))
                    pygame.draw.line(screen,(255,255,255),pos_prev,pos_next,2)
                    pos_prev=pos_next
            else:
                end=(int(pos_next[0]*1000/xlimit),int(pos_next[1]*1000/ylimit))
                pygame.draw.line(screen,(255,255,255),pos_next,pos_next,2)
                pos_prev=pos_next
        print(pos_prev)        
        cv2.imshow('output', drawing)
        cv2.imshow('photu',imager)
    # Keyboard OP
    k = cv2.waitKey(10)
    if k == 27:  # press ESC to exit
        camera.release()
        cv2.destroyAllWindows()
        break
    elif k == ord('b'):  # press 'b' to capture the background
        bgModel = cv2.createBackgroundSubtractorMOG2()
        isBgCaptured = 1
        print( '!!!Background Captured!!!')
    elif k == ord('r'):  # press 'r' to reset the background
        bgModel = None
        triggerSwitch = False
        isBgCaptured = 0
        print ('!!!Reset BackGround!!!')
    pygame.display.flip()
