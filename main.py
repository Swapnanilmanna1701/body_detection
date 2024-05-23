import cv2
from cvzone.PoseModule import PoseDetector
detector = PoseDetector()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = detector.findPose(frame)
    lmList, bboxInfo = detector.findPosition(frame, bboxWithHands = True)
    cv2.imshow("Image", frame)
    cv2.waitKey(1)