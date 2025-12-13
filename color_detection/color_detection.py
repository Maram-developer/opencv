#not good

import cv2
cap=cv2.VideoCapture(0)



while True:
    succ,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    

    h,w,_=frame.shape
    center_x=int(h/2)
    center_y=int(w/2)
    pixel_center_color=frame[center_x,center_y]
    h_color=pixel_center_color[0]
    s_color=pixel_center_color[1]
    v_color=pixel_center_color[2]
    
    color="undefind"
    if h_color<5:
        color="red"
    elif s_color<40:
        color="whire"
    elif v_color<20:
        color="black"
    elif h_color<22:
        color="orange"
    elif h_color<43:
        color="yellow"
    elif h_color<75:
        color="green"
    elif h_color<129:
        color="blue"
    elif h_color<170:
        color="violet"
    else:
        color="no recognition"
        
    pixel_center_bgr=frame[center_y,center_x]
    
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    cv2.putText(frame,color,(100,100),0,4,( b,g,r),6)
    print(pixel_center_color)
    cv2.circle(frame,(center_x,center_y),10,(100,200,100),6)
    
    cv2.imshow("frame",frame)
    kay=cv2.waitKey(1)
    if kay==ord('q'):
        break
