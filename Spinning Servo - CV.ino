/***********************

Spinning Servo:

  This project receives a servo angle from a python file using the serial port and spins the
  servo depending on the angle. The servo angle is determined using handtracking from a webcam and opencv.

  **Author: Vish Chaudhary **
  **Github: https://github.com/VishChaudhary **

************************/

#include <cvzone.h>
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
SerialData serialData(1, 3); //(number of values received, digits per value)
int recPos[1];  //array received position with size of number of values received

void setup() {
 pinMode(9, OUTPUT);
 myservo.attach(9);    // attaches the servo on pin 9 to the servo object
 serialData.begin(9600);
}

void loop() {
  serialData.Get(recPos);
  myservo.write(recPos[0]);
}