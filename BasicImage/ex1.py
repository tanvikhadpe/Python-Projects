import cv2
import imutils
img = cv2.imread("sample.jpg") #read an image
resizeImg = imutils.resize(img,width=20) #resize
cv2.imwrite("resizedImage.jpg",resizeImg) #saving
