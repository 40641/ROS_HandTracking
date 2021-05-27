import cv2
import mediapipe as mp
import time

import math
import rospy
from std_msgs.msg import String


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.8, trackCon=0.8):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)



        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True, ):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]



            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy =round(float(lm.x*w/1000), 3), round(float(lm.y*h/1000), 3)

                #print(id, cx, cy)
                # lmList.append([id, cx, cy])
                lmList.append([cx, cy])


                # if draw:
                #     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)


        return lmList

def main():
    pTime = 0
    cTime = 0


    cap = cv2.VideoCapture(-1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    detector = handDetector()




    while True:
        try:
            #actual_tcp_pose = rtde_r.getActualTCPPose()

            success, img = cap.read()
            img = detector.findHands(img)

            lmList = detector.findPosition(img)
            #asd = lmList[0]
            lofasz = lmList[0][0]
            xdd = lmList[0][1]
            if len(lmList) != 0:

                x_cord = lmList[0][0]
                y_cord = lmList[0][1]
            
                # x1_cord = lmList[4][0]
                # y1_cord = lmList[4][1]

                # x2_cord = lmList[8][0]
                # y2_cord = lmList[8][1]

                # lenght = round(math.sqrt((x2_cord-x1_cord)**2+(y2_cord-y1_cord)**2), 3)



                # if lenght < 0.06:

                #     gripper = "close"
                # else:

                #     gripper = "open"

            
                #print(x_cord, y_cord, gripper)
                #print(x_cord, y_cord)
                #print(lenght)
            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (10,30), cv2.FONT_HERSHEY_PLAIN,2, (0,0,255), 2)


            cv2.imshow("image", img)

            cv2.waitKey(1)
            return lofasz, xdd
        
        except:
                continue
        
if __name__ == "__main__":
    main()
