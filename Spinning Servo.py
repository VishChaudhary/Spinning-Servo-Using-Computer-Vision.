#   Spinning Servo:
#
#       This project uses the distance between the pads of your thumb and index finger to spin a servo connected to
#   an Arduino. Additionally, if the thumb is closed: if 1 finger is up then the servo is spun to 45 degrees,
#   if 2 fingers are up then the servo is spun to 90 degrees, 3 fingers- 135 degrees, and 4 fingers - 180 degrees (Max).
#   The servo angle is determined using the webcam and accurately tracks the hand using opencv. The servo angle is sent
#   to the arduino board using the serial port.

#   Author: Vish Chaudhary
#   Github: https://github.com/VishChaudhary






import numpy
import cv2
from cvzone.SerialModule import SerialObject
import HandTrackingModule as mod

cap = cv2.VideoCapture(0)   #capture video from built in camera
detector = mod.handDetector(detectionCon=0.75)
arduino = SerialObject('/dev/cu.usbmodem141201')
servo_position = 0
while True:

    #1. Import image
    success, img = cap.read()  # read image into img
    img = cv2.flip(img, 1) #flips the image in the first direction (horizontal direction)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, False)
    present_hand = detector.handedness(img)

    if len(lmList) != 0:  # will print the pixel position only if a hand is present. Checks to see if a hand is present.
        fingers_up = detector.fingerCounter()
        # tip of index finger
        x1, y1 = lmList[8][1:]  # x1, y1 is the tip coordinates of the index finger. [8] is landmark 8 which is the index
        # finger. [1:] from element 1 till the end. Theres 3 elements but the count starts at zero so 1 referes to element 2.
        # tip of thumb
        x2, y2 = lmList[4][1:]

        # If all fingers are closed (fist made) then spin servo to 0 degrees.
        if fingers_up.count(1) == 0:
            servo_position = 0

        # If thumb closed and 1 fingers up spin servo to 45 degrees.
        elif fingers_up[0] == 0 and fingers_up.count(1) == 1:
            servo_position = 45

        # If thumb closed and 2 fingers up spin servo to 90 degrees.
        elif fingers_up[0] == 0 and fingers_up.count(1) == 2:
            servo_position = 90

        # If thumb closed and 3 finger up spin servo to 135 degrees.
        elif fingers_up[0] == 0 and fingers_up.count(1) == 3:
            servo_position = 135

        # If thumb closed and 4 finger up spin servo to 180 degrees (Max).
        elif fingers_up[0] == 0 and fingers_up.count(1) == 4:
            servo_position = 180

        # If thumb and index finger both open the spin servo depending on the angle between their finger pads.
        elif fingers_up[0] == 1 and fingers_up[1] == 1:
            change_x = abs(x2-x1)
            change_y = abs(y2-y1)
            fingers_distance = int(numpy.hypot(change_y, change_x))
            cv2.line(img, (x1, y1), (x2, y2), (255, 113, 82), 6)
            cv2.circle(img, (x1, y1), 20, (255, 113, 82), cv2.FILLED)
            cv2.circle(img, (x2, y2), 20, (255, 113, 82), cv2.FILLED)
            servo_position = int(numpy.interp(fingers_distance, [35, 320], [0, 180], left=0, right=180))

        cv2.putText(img, 'Servo Angle:' + str(servo_position), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (22, 22, 255), 2)
        arduino.sendData([servo_position])

    cv2.imshow('My Webcam', img)  # show the image
    cv2.waitKey(1)  # one millisecond delay
