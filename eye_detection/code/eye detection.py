import cv2
cap = cv2.VideoCapture("D:/NU comptetion/computer vision/eye.mp4")

while True:
    ret,frame=cap.read()
    if ret is False:
        break
    frame=cv2.resize(frame,(800,600))
    row,cols,_=frame.shape
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(7,7),0)
    _,threshold=cv2.threshold(blur,3,200,cv2.THRESH_BINARY_INV)
    contours,hr=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)
    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.drawContours(frame,[cnt],-1,(0,0,255),3)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.line(frame,(x+int(w/2),0),(x+int(w/2),row),(0,255,0),2)
        cv2.line(frame,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break
    cv2.imshow("threshold",threshold)
    cv2.imshow("gray",gray)
    cv2.imshow("original",frame)
    key=cv2.waitKey(30)
    if key==ord('q'):
        break
  
cv2.destroyAllWindows()
        