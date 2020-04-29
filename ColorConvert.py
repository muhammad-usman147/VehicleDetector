import cv2
import os
def ConvertToGray():
    data = os.listdir('n/')

    for i in data:
        cv2.imwrite(i,cv2.imread('n/{}'.format(i),0))

def RenammeImages():
    n = os.listdir('n/')
    p = os.listdir('p/')
    for i,img in enumerate(n):
        os.rename('n/{}'.format(img),'n/neg{}.jpg'.format(i))

def DetecVehicle():
    vc = cv2.CascadeClassifier('classifier/Cascade.xml')
    img = cv2.imread('2.png',0)
    detect = vc.detectMultiScale(
    img,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(15,15),
    flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x,y,w,h) in detect:
        img = cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),2)
    cv2.imshow('fa',img)
    cv2.waitKey(0)
DetecVehicle()
cv2.destroyAllWindows()