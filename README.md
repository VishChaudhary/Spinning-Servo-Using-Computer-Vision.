# Spinning-Servo-Using-Computer-Vision.

# Author: Vish Chaudhary

Demo: https://youtu.be/WGUpUfKPl5Q


This project uses opencv and my hand detection module to spin a servo depending on the distance between the tips of the thumb and index finger. Other specific angles can also be achieved.

 Spinning Servo:

This project uses the distance between the pads of your thumb and index finger to spin a servo connected to
an Arduino. Additionally, if the thumb is closed: if 1 finger is up then the servo is spun to 45 degrees,
if 2 fingers are up then the servo is spun to 90 degrees, 3 fingers- 135 degrees, and 4 fingers - 180 degrees (Max).
The servo angle is determined using the webcam and accurately tracks the hand using opencv. The servo angle is sent
to the Arduino board using the serial port.

Github: https://github.com/VishChaudhary
