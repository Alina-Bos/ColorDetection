from cv2 import cv2

#importing numpy for numerical processing
import numpy as np


img_path = "F:/Documents/Lina/Hobby/ColorDetection/Pic1.jpg"
img = cv2.imread(img_path)
clicked = False
r = g = b = xpos = ypos = 0
cv2.namedWindow("Color Detection")


#creating RGB values of the pixel when we double click it
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#setting up the actual mouse click
cv2.setMouseCallback("Color Detection", draw_function)

while(1):

    cv2.imshow("Color Detection", img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = ("R = " + str(r) + ", G = " + str(g) + ", B = " + str(b))
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #leaves the program if esc is pressed
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()