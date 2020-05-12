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
screen=pygame.display.set_mode([1000,1000])
running=True
screen.fill((255,255,255))
click=False
pos_prev=None
# variables
isBgCaptured = 0   # bool, whether the background captured
triggerSwitch = False  # if true, keyborad simulator works
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([255,173,127],np.uint8)
clock = pygame.time.Clock()
realdraw=screen.copy()
canvas = screen.copy()
orig=(500,500)
def printThreshold(thr):
    print("! Changed threshold to "+str(thr))

def skindet(frame):
    image_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #model_hsv = image_hsv[225:275,625:675] # Select ROI

#Get the model histogram M
    M = cv2.calcHist([image_hsv], channels=[0, 1], mask=None, histSize=[80, 256], ranges=[0, 180, 0, 256] )
#Backprojection of our original image using the model histogram M
    B = cv2.calcBackProject([image_hsv], channels=[0,1], hist=M, 
                         ranges=[0,180,0,256], scale=1)
    D = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(B, -1, D, B)
#Threshold to clean the image and merging to three-channels
    _, thresh = cv2.threshold(B, 30, 255, cv2.THRESH_BINARY)
    #cv2.imwrite("/assets/img/skin-detection/roi.png",cv2.cvtColor(model_hsv,cv2.COLOR_HSV2RGB))
    picture=cv2.bitwise_and(frame,frame, mask = thresh)
    cv2.imshow('skinpic',picture)
    picture=cv2.cvtColor(picture,cv2.COLOR_HSV2BGR)
    picture=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('histo',picture)
    return picture
def removeBG(frame):
    fgmask = bgModel.apply(frame,learningRate=-1)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    imageYCrCb = cv2.cvtColor(res,cv2.COLOR_BGR2YCR_CB)
    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
    ansImg = cv2.bitwise_and(res,res, mask = skinRegion)
    ansImg=skindet(ansImg)
    kernel = np.ones((8, 8), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    #fgmask = cv2.equalizeHist(fgmask)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    #gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(ansImg, (5, 5), 0)
    #gray=ansImg
    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, kernel2, iterations=2)
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
    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),(frame.shape[1], int(ylimit)), (255, 0, 0), 2)
   # cv2.imshow('original', frame)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #  Main operation
    if isBgCaptured == 1:  # this part wont run until background captured
        #img = imager[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
        frame=frame[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]
        imager=removeBG(frame)
        #cv2.imshow('mask', img)
        img = imager
        newx=1000
        newy=1000
        newsize = (newx, newy) 
        img = cv2.resize(img,newsize)
        frame = cv2.resize(frame,newsize)
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
        drawing = np.zeros(img.shape, np.uint8)
        minDist = []
        #print(length)
        if length > 0:
            #res = max(contours, key=cv2.contourArea)
            res=0
            if pos_prev is not None:
                for i in range(length):  # find the biggest contour (according to area)
                    temp = contours[i]
                    area = cv2.contourArea(temp)
                    print("area :",area)
                    M = cv2.moments(temp)
                    #cX = int(M['m10'] /M['m00'])
                    #cY = int(M['m01'] /M['m00'])
                    top= tuple(temp[temp[:, :, 1].argmin()][0])
                    cX=top[0]
                    cY=top[1]
                    print(pos_prev,"*******",top)
                    dx = abs(pos_prev[0] - cX)
                    dy = abs(pos_prev[1] - cY)
                    #D = np.sqrt(dx*dx+dy*dy)
                    print(dx,"---",dy)        
                    if(dx < 50 and dy<50):
                        cv2.drawContours(frame, temp, 0, (255, 255, 0), 2)
                        minDist.append(temp)
                if len(minDist)>0: 
                    res= max(minDist, key=cv2.contourArea)
                else:
                    print("Not")
            else:
                pos_prev=(500,500)         
            if len(minDist)>0:             
                hull = cv2.convexHull(res)
                #cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
                #cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)
                m=10000
                pos=0
                for i in range(hull.shape[0]):
                    if hull[i][0][1]<m:
                        m=hull[i][0][1]
                        pos=i
                pos_next=tuple(hull[pos][0])
                cv2.circle(drawing, pos_next, 3, (255,255,255), 3)
                if  pos_prev is not None:
                    pygame.draw.rect(canvas, (128,128,128), (pos_prev[0]*1000/newx,pos_prev[1]*1000/newy,15,15))       
                    screen.blit(canvas, (0, 0))
                    canvas.fill((255,255,255))    
                    if(abs(pos_prev[0]-pos_next[0])<=100 and abs(pos_prev[1]-pos_next[1])<=100): 
                        end=(int(pos_next[0]*1000/newx),int(pos_next[1]*1000/newy))
                        print(abs(orig[0]-end[0]))
                        #if(abs(orig[0]-end[0])>20*500/xlimit or abs(orig[1]-end[1])>20*500/ylimit):
                        pygame.draw.line(realdraw,(0,0,0),orig,end,7)
                        orig=(int(pos_next[0]*1000/newx),int(pos_next[1]*1000/newy))
                        pos_prev=pos_next
                    canvas.blit(realdraw, (0, 0))        
                else:
                    #orig=(int(pos_prev[0]*1000/xlimit),int(pos_prev[1]*1000/ylimit))
                    end=(int(pos_next[0]*1000/newx),int(pos_next[1]*1000/newy)) 
                    orig=(int(pos_next[0]*1000/newx),int(pos_next[1]*1000/newy))
                    pygame.draw.line(realdraw,(0,0,0),end,end,7)
                    pos_prev=pos_next
        #print(pos_prev)        
        #cv2.imshow('output', drawing)
        cv2.circle(frame, pos_prev, 3, (255,0,0), 10)
        cv2.imshow('photo',frame)
        cv2.imshow('mask',img)
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
    #canvas.fill((255,255,255))
    pygame.display.flip()
