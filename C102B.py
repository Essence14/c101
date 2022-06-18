from tkinter import Frame
import cv2

def takeSnapshot():
    vco=cv2.VideoCapture(0)
    result=True
    while(True):
        Ret,Frame=vco.read()
        cv2.imwrite("img.jpg",Frame)
        #result=False
    vco.release()
    cv2.destroyAllWindows()

takeSnapshot()