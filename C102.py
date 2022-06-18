import time
import dropbox
import random
import cv2
from numpy import true_divide

starttime=time.time()

def takeSnapshot():
    N=random.randint(0,100)
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        Ret,Frame=vco.read()
        imagename="img"+str(N)+".png"
        cv2.imwrite(imagename,Frame)
        starttime=time.time
        result=False
    return imagename
    print("Snapshot Taken")
    vco.release()
    cv2.destroyAllWindows()
    
def uploadFile(img):
    accessToken="sl.BJyIKfNAOb-V-Zqznr7iMT57JsOgGhkyWObSo0EqXgQuhVPN5-SRbD4w3tCHs9ggNTry9ydWrspZqgQ-jqbu40AnssM1YsVK4dA2uN0z71u7VziPodHWz0vfAotYWs-5SZYBH0JNuL-U"
    dbx=dropbox.Dropbox(accessToken)
    file=img
    fileto="/img/"+(img)
    with open(file,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")

def main():
    while(True):
        if((time.time()-starttime)>=30):
            name=takeSnapshot()
            uploadFile(name)

main()