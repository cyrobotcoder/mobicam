import cv2
import numpy as np
url = "enter the ip address shown in the app/video"
cp=cv2.VideoCapture(url)
while(True):
    ret , frame= cp.read()
    if frame is not None:
        cv2.imshow("frame",frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
