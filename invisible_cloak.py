import cv2
import time
import numpy as np

# Saving the output in a file 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# Starting the webcam
cap=cv2.VideoCapture(0)
time.sleep(2)
bg=0

# Capturing the background for 60 frames
for i in range(60):
    ret_bg=cap.read()
bg=np.flip(bg,axis=1)

# Reading the captured frames until the camera is opened

while(cap.isOpened()):
    ret_img=cap.read()
    if not ret:
        break
    # Flipping the image for consistency
    img=np.flip(img,axis=1)
    # Converting from bgr to hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Generating mask to detect red color
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)
    mask1=mask1+mask2
    # Open and expand the image where there is mask 1
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint(8)))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint(8)))

    # Selecting the part that does not have mask 1 and saving in mask 2

    mask2=cv2.bitwise_not(mask1)

    # Keeping only the part of the image without the red color

    result=cv2.bitwise_and(img,mask=mask2)
    result2=cv2.bitwise_and(bg,mask=mask1)

    # Generating the final output by merging result and result2

    final=cv2.addWeighted(result,1,result2,1,0)
    output_file.write(final)
    cv2.imshow('Magic',final)
    cv2.waitKey(1)
cap.release()
#out.release()
cv2.destroyAllWindows()