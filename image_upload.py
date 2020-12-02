# importing OpenCV(cv2) module 
from cv2 import cv2

# Save image in set directory, so that we can actually open it later 
# Read RGB image 
img = cv2.imread('Pic1.jpg')  
  
# Output img with window name as 'image' 
cv2.imshow('WaterColor', img)  
  
# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)         
  
# Destroying present windows on screen 
cv2.destroyAllWindows()  