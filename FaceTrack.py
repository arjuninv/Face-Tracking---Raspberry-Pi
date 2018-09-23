import cv2
import picamera
import time
import sys
import RPi.GPIO as GPIO
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
px = GPIO.PWM(3, 50)
px.start(6)
py = GPIO.PWM(5, 50)
py.start(8)


tx = 6
ty = 8

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
ret, img = cap.read() 



if not cap:
    print("VideoCapture failed...")
    sys.exit()
try:
    
    while 1:
        
        ret, img = cap.read() 
        
         if ret is True:
            #working with grayscale image is much faster, and is a better choice for computer like raspberry pi.
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            continue
     
        cv2.rectangle(img,(320,250),(321,251),(255,255,0),2) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #The program lets the camera point at your face in both x and y axis. In X axis, coordinates from 100 to 200 is set to be the centre. 
        #For Y axis, the centre coordinates are from 120 to 180. It is recomended that you try different values according to your camera and servo motor and choose what works best for you.
        
 
        for (x,y,w,h) in faces:
            
            xn = (x + x + w) / 2
            if(xn > 200):
                if(tx > 2):
                    print "Hleft" +  str(xn) + "  -  " + str(abs((abs(200 - xn) / 10) - 5))
                    tx = tx - 0.2
                    px.ChangeDutyCycle(tx)
                    
                else:
                    px.ChangeDutyCycle(0)
              
            elif(xn < 100):
                print "Hright" + str(xn) + "  -  " + str(abs((abs(200- xn) / 10) - 10))
                if(tx < 11):
                    tx = tx + 0.2
                    px.ChangeDutyCycle(tx)
                    
                else:
                    px.ChangeDutyCycle(0)
            else:
                px.ChangeDutyCycle(0)
                print "Hgood" + str(xn)
            

            yn = (y + y + h) / 2
            if(yn > 180):
                
                if(ty > 2):
                    print "Vleft" +  str(yn) + "  -  " + str(abs((abs(200 - yn) / 10) - 5))
                    ty = ty - 0.2
                    py.ChangeDutyCycle(ty)
                    #time.sleep(0.5)
                else:
                    py.ChangeDutyCycle(0)
              
            elif(yn < 120):
                print "Vright" + str(yn) + "  -  " + str(abs((abs(200- yn) / 10) - 10))
                if(ty < 11):
                    ty = ty + 0.2
                    py.ChangeDutyCycle(ty)
                    #time.sleep(0.5)
                else:
                    py.ChangeDutyCycle(0)
            else:
                py.ChangeDutyCycle(0)
                print "Vgood" + str(yn)
                
            time.sleep(0.1)
            break
                
         
   
except KeyboardInterrupt:
    pass
 

cap.release()
 
GPIO.cleanup()  
cv2.destroyAllWindows() 
