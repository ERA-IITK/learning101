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
##clock = pygame.time.Clock()
realdraw=screen.copy()
canvas = screen.copy()
smoothDraw=screen.copy()
orig=(500,500)
drawpermit=False
scale=False
hand_hist = None
traverse_point = []
total_rectangle = 9
hand_rect_one_x = None
hand_rect_one_y = None
hand_rect_two_x = None
hand_rect_two_y = None
is_hand_hist_created = False
counterforsmoothing=0
penImage=pygame.image.load('pen.png')
pygame.display.set_icon(penImage)
black=(0,0,0)
violet=(58,0,84)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
color=black
thick=7
distprev=(0,0)
def nothing(x):
    pass
def skindet(frame):
    global hand_rect_one_x, hand_rect_one_y
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    roi = np.zeros([90, 10, 3], dtype=hsv_frame.dtype)

    for i in range(total_rectangle):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv_frame[hand_rect_one_x[i]:hand_rect_one_x[i] + 10,hand_rect_one_y[i]:hand_rect_one_y[i] + 10]

    hand_hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    return cv2.normalize(hand_hist, hand_hist, 0, 255, cv2.NORM_MINMAX)

def draw_rect(frame):
    rows, cols, _ = frame.shape
    tempo=frame
    global total_rectangle, hand_rect_one_x, hand_rect_one_y, hand_rect_two_x, hand_rect_two_y

    hand_rect_one_x = np.array([6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,12 * rows / 20, 12 * rows / 20], dtype=np.uint32)

    hand_rect_one_y = np.array([9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,10 * cols / 20, 11 * cols / 20], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10

    for i in range(total_rectangle):
        cv2.rectangle(tempo, (hand_rect_one_y[i], hand_rect_one_x[i]),(hand_rect_two_y[i], hand_rect_two_x[i]),(0, 255, 0), 1)
    return tempo

def hist_masking(frame, hist):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    cv2.filter2D(dst, -1, disc, dst)
    ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)
    # thresh = cv2.dilate(thresh, None, iterations=5)
    thresh = cv2.merge((thresh, thresh, thresh))
    return cv2.bitwise_and(frame, thresh)
def removeBG(frame):
    global hand_rect_one_x,hand_rect_one_y,maskp
    #newimg=hist_masking(frame,hand_hist)
    fgmask = bgModel.apply(frame,learningRate=-1)
    kernel2 = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel2, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    hist_mask_image = hist_masking(res, hand_hist)
    kernel = np.ones((16, 16), np.uint8)
    gray=hist_mask_image
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    #thresh = cv2.erode(thresh, kernel2, iterations=2)
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    ##cv2.imshow('onlyhist',hist_mask_image)
    ##cv2.imshow('onlybg',res)
    return thresh

# Camera
camera = cv2.VideoCapture(0)
camera.set(10,200)
cv2.namedWindow('thickness_brush')
cv2.createTrackbar('trh1', 'thickness_brush', thick, 100, nothing)
while camera.isOpened() and running:
    ret, frame = camera.read()
    if(is_hand_hist_created==False):
        show_frame = draw_rect(frame)
        show_frame=cv2.flip(show_frame,1)
    thick = cv2.getTrackbarPos('trh1', 'thickness_brush')    
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
    if is_hand_hist_created == True:  # this part wont run until background captured
          # clip the ROI
        frame=frame[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  
        imager=removeBG(frame)
        ##imager=hist_mask_image#[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]
        cv2.imshow('masker', imager)
        #img = imager[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]
        img = cv2.cvtColor(imager,cv2.COLOR_HSV2BGR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img=imager
        newx=1000
        newy=1000
        newsize = (newx, newy) 
        img = cv2.resize(img,newsize)
        frame = cv2.resize(frame,newsize)
        # get the coutours
        thresh1 = copy.deepcopy(img)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        drawing = np.zeros(img.shape, np.uint8)
        minDist = []
        #print(length)
        if length > 0:
            res = max(contours, key=cv2.contourArea)
            #res=0
            if pos_prev is not None:
                for i in range(length):  # find the biggest contour (according to area)
                    temp = contours[i]
                    area = cv2.contourArea(temp)
                    M = cv2.moments(temp)
                    top= tuple(temp[temp[:, :, 1].argmin()][0])
                    cX=top[0]
                    cY=top[1]
                    #print(pos_prev,"*******",top)
                    dx = abs(pos_prev[0] - cX)
                    dy = abs(pos_prev[1] - cY)
                    #D = np.sqrt(dx*dx+dy*dy)
                    #print(dx,"---",dy)        
                    if(dx < 50 or dy<50):
                        cv2.drawContours(frame, temp, 0, (255, 255, 0), 2)
                        minDist.append(temp)
                if len(minDist)>0: 
                    res= max(minDist, key=cv2.contourArea)    
            else:
                pos_prev=(500,500)         
            if len(minDist)>0:             
                hull = cv2.convexHull(res)
                m=10000
                pos=0
                for i in range(hull.shape[0]):
                    if hull[i][0][1]<m:
                        m=hull[i][0][1]
                        pos=i
                pos_next=tuple(hull[pos][0])
                if  pos_prev is not None:           
                    if(abs(pos_prev[0]-pos_next[0])<=100 and abs(pos_prev[1]-pos_next[1])<=100): 
                        end=(orig[0]-int((pos_prev[0]-pos_next[0])*1000/newx),orig[1]-int((pos_prev[1]-pos_next[1])*1000/newy))
                        if(drawpermit):
                            pygame.draw.line(realdraw,color,orig,end,thick)
                            screen.blit(realdraw, (0, 0))
                            if(counterforsmoothing==0):
                                distprev=orig
                            elif(counterforsmoothing==3):
                                pygame.draw.line(smoothDraw,color,distprev,end,thick)
                                realdraw.blit(smoothDraw, (0, 0))
                                counterforsmoothing= -1    
                            counterforsmoothing= counterforsmoothing+1 
                            #print(distprev)
                        else:
                            counterforsmoothing= 0
                        orig=end
                        pos_prev=pos_next
                        pygame.draw.rect(screen, (128,128,128), (orig[0],orig[1],15,15))        
                else:
                    end=(orig[0]-int((pos_prev[0]-pos_next[0])*1000/newx),orig[1]-int((pos_prev[1]-pos_next[1])*1000/newy))
                    orig=(int(pos_next[0]*1000/newx),int(pos_next[1]*1000/newy))
                    if(drawpermit):
                        pygame.draw.line(realdraw,(0,0,0),end,end,thick)
                    pos_prev=pos_next
        cv2.circle(frame, pos_prev, 3, (255,0,0), 40)
        cv2.imshow('mask',img)
    # Keyboard OP
    if(is_hand_hist_created):
        frame=cv2.resize(frame,(500,500))
        cv2.imshow('photo',frame)
    else:
        cv2.imshow('photo',show_frame)
    k = cv2.waitKey(1)
    if k == 27:  # press ESC to exit
        camera.release()
        cv2.destroyAllWindows()
        break
    elif k == ord('b'):  # press 'b' to capture the background
        color=black
    elif k == ord('v'):
        color=violet
    elif k == ord('r'):
        color= red
    elif k == ord('g'):
        color=green            
    elif k == ord('d'):
        if(drawpermit):
            drawpermit=False
        else:
            drawpermit=True    
        print("Start")    
    elif k == ord('e'):
        color=white
    elif k == ord('z'):
        is_hand_hist_created = True
        hand_hist = skindet(show_frame)                    
        bgModel = cv2.createBackgroundSubtractorMOG2()
        isBgCaptured = 1
        print( '!!!Background Captured!!!')
    pygame.display.flip()