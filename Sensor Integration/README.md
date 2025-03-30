# Arm Kinematics
Contains all the necessary code for communicating with the hardware and manipulating the rover kinematics. All of these are based on Arduino and use Pyfirmata to connect Python to Arduino. Before running any code,

- Install the Firmata library on Arduino IDE. The Firmata library implements the Firmata protocol for communicating with software on the host computer.
- Upload the *Standard Firmata* code to the connected Arduino board from *Examples/Firmata/* in the menu. 

Use pyfirmata2 with Arduino wherever necessary. More instructions are detailed in [USAGE.md](USAGE.md).

## Contents

- Inverse Kinematics (with [one hinge](inverse%20kinematics/inverse_kin%202%20arms.py) and [two hinges](inverse%20kinematics/inverse_kin%203%20arms.py))
- [Working arm controller](arm_working.ipynb) (rotates the arm to a given $(x,y,z)$ coordinate)
- [Manipulator Base Alignment](basealign.py) (rotates the arm base to a given angle)
- Arduino Integrations
  - [Servo Motor](servo/servo.py)
  - [Ultrasonic Sensor](ultrasonic/ultrasonic.py)
  - Stepper Motor ([A4988 driver](StepperLib.py))
  - [DC Motor](dcmotor_encoder.py)
  - [MPU 6050](mpu6050.py) (accelerometer and gyroscope module)
  - [NRF 2401](nrf.py) (wireless transceiver)
