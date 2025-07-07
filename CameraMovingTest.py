#Camera Moving Test

import cv2   #opencv

import imutils  #resise

cam = cv2.VideoCapture(0)   #open primary camera

firstFrame=None
area = 500

while True:
     _,vid = cam.read()
     text="Normal"

  

     vid=imutils.resize(vid,width=1000)
     #print("am came")

     grayImg=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)

     smooth=cv2.GaussianBlur(grayImg,(21,21),0)

     if firstFrame is None:
          firstFrame=smooth
          continue

     #Difference
     imgDiff = cv2.absdiff(firstFrame,smooth)

     threshold=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]

     threshold=cv2.dilate(threshold,None,iterations=2)
     
                                                       #outer area         compress and memory save
     contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

     contours=imutils.grab_contours(contours) #store all contours

     for c in contours:
          if cv2.contourArea(c) < area:
               continue
          (x,y,w,h)=cv2.boundingRect(c) # getting coorinates for current contours

          cv2.rectangle(vid,(x,y),(x+w,y+h),(0,255,0),2)
          text="Object Detected"
     print(text)

     cv2.putText(vid,text,(15,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

     cv2.imshow("CameraRunning",vid)

     key=cv2.waitKey(10)

     if key == ord("x"):
          break

cam.release()
cv2.destroyAllWindows()  #close all windows

          
          

