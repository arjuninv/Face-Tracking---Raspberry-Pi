# Face-Tracking---Raspberry-Pi
I originally used it my project - J.A.R.V.I.S, an artificial intelligence powered home assistant. Check out this video to see it in action - https://www.youtube.com/watch?v=eWdhU5LIsBI

# Use:
FaceTrack.py lets raspberry pi always point the camera at a person's face once detected. It makes use of the OpenCV library available for python.

# Assembly:
Its fairly simple to set up and use, and you can make some tweeks and calibrate the varibales so that it works smoothly on your project too.
  
# Notes:
The program lets the camera point at your face in both x and y axis. 
In X axis, coordinates from 100 to 200 is set to be the centre. 
In Y axis, the centre coordinates are from 120 to 180.
It is recomended that you try different values according to your camera and servo motor and choose what works best for you.
You can delay of around 0.5 seconds after moving the servo each time. For me, the servo's rotation was jittery so I didn't.
        
 
  
