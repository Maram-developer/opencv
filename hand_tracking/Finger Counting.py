import cv2
import mediapipe as mp
tips=[4,8,12,16,20]
cam =cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
while True:
    succ,img=cam.read()
    img=cv2.flip(img,1)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    resuls=hands.process(imgrgb)
    lmList=[]
    if resuls.multi_hand_landmarks:
        for handlms in resuls.multi_hand_landmarks:
            for id ,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x *w),int(lm.y*h)
                lmList.append([id,cx,cy])
                
                
                mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
               #if id == 8:
                #   cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
                if len(lmList) ==21:
                    
                    fingers =[]
                    if lmList[tips[0]][1] <  lmList[tips[0] - 2][1]  :
                        fingers.append(1)
                    else :
                        fingers.append(0)
                    for tip in range(1,5):
                        if lmList[tips[tip]][2] < lmList[tips[tip] - 2][2]:
                            fingers.append(1)

                        else:
                            fingers.append(0)
                    
                    totalFingers=fingers.count(1)
                    
                    cv2.putText(img,f'{totalFingers}',(100,100),cv2.FONT_HERSHEY_SIMPLEX,3,(100,200,100),5)
                        
    cv2.imshow("hand_tracking",img)
    if cv2.waitKey(5) & 0xff==ord('q'):
        break