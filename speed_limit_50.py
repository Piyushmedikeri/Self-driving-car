import numpy as np
import cv2

stop_cascade = cv2.CascadeClassifier('speed_limit_50.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT
count=0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

    # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        stop = stop_cascade.detectMultiScale(gray, 1.3, 4)

        for (x,y,w,h) in stop:
            if ((x>0)or(y>0)or(h>0)or(w>0)):
                count+=1
                print ("speed limit 50")
                if(count==1):
                    break
      
   
        for (x,y,w,h) in stop:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
