# Usage Guide

This document provides an overview of the different Python modules in this project and how to use them. Almost everything here uses `pyfirmata2` to communicate with an Arduino board, so make sure to install and understand `pyfirmata2` before proceeding.

## Using `pyfirmata2`

`pyfirmata2` is a Python interface for Firmata, a protocol used for communication between a microcontroller (like an Arduino) and a host computer.

### Installing `pyfirmata2`

```bash
pip install pyfirmata2
```

**Note:** There are ipynb files which you can refer to for a better understanding of how to integrate the modules.

### Example Usage

```python
from pyfirmata2 import Arduino, util

board = Arduino('/dev/ttyUSB0')  # Replace with your port
iterator = util.Iterator(board)
iterator.start()

pin = board.get_pin('d:13:o')  # Digital pin 13 as output
pin.write(1)  # Turn LED on
```

Most of the modules in this project rely on `pyfirmata2` for communication with the Arduino.

## Module Overview

### 1. `StepperLib.py`
**Description:** This module provides functionality for controlling stepper motors using the A4988 driver or ULN2003 driver with an Arduino board.

#### `Stepper` Class
**Usage:**
```python
from StepperLib import Stepper

# Example usage
stepper = Stepper(board, dir_pin=8, step_pin=7, micro_step_pins=(2, 3, 4), total_steps=200)
stepper.turn_angle(90)  # Rotate motor by 90 degrees
```

- `set_delay(delay)`: Sets the step delay time.
- `switch_direction()`: Reverses the motor direction.
- `turn_angle(angle)`: Rotates the motor by a given angle.
- `step(steps)`: Moves the motor by a specified number of steps.
- `set_resolution(resolution)`: Adjusts the microstepping resolution.

#### `Stepper_ULN2003` Class
**Usage:**
```python
from StepperLib import Stepper_ULN2003

# Example usage
stepper = Stepper_ULN2003(board, pins=(8, 9, 10, 11))
stepper.rotate(num_rotations=2, direction=True)  # Rotate clockwise for 2 full rotations
```

- `rotate(num_rotations, direction)`: Rotates the stepper motor by a given number of rotations in the specified direction.

---

### 2. `ultrasonic.py`
**Description:** This module interfaces with an ultrasonic sensor to measure distances.

#### `ultrasonic` Class
**Usage:**
```python
from ultrasonic import ultrasonic

# Example usage
sensor = ultrasonic(trigger_pin=7, echo_pin=8, board=board)
distance = sensor.read_distance()
print(f"Distance: {distance} cm")
```
---

### 3. `servo.py`
**Description:** This module provides functionality to control a servo motor using an Arduino.

#### `Servo` Class
**Usage:**
```python
from servo import Servo

# Example usage
servo = Servo(board, pin=9)
servo.turn_angle(90)  # Move servo to 90 degrees
```

---

### 4. `basealign.py`
**Description:** This module calculates the base alignment angle for a rover's arm based on its position.

#### `alignbase` Class
**Usage:**
```python
from basealign import alignbase

# Example usage
base = alignbase(20, 30)
angle = base.calculate_angle(-30, 40)
aligned_angle = base.align_robot(-30, 40)
arm_angle = base.align_robot_arm(10, -30)
```

- `calculate_angle(x2, z2)`: Computes the angle between the base and a target point `(x2, z2)`.
- `align_robot(target_x, target_z)`: Returns the angle needed to align the rover base with a target.
- `align_robot_arm(arm_x, arm_z)`: Computes the relative angle for the robot arm.

---

### 5. `dcmotor_encoder.py`
**Description:** This module provides functionality for controlling a DC motor with an encoder using an Arduino board. However, it is not completely or correctly developed yet.

#### Functionality:
- Reads encoder values to track motor position.
- Controls motor speed and direction using PWM and digital signals.

**Usage:**
```python
from dcmotor_encoder import control_motor

# Example usage
control_motor(0.5, 1)  # Set motor speed to 50% and rotate clockwise
```

#### Functions:
- `control_motor(speed, direction)`: Controls the motor speed (0-1) and direction (0: counter-clockwise, 1: clockwise).
- Encoder readings are handled in a background thread to track motor position.

---

### 6. `force.py`
**Description:** This module reads the force sensor output using pyfirmata2.

**Usage:**
```python
from force import read_force

# Example usage
force_value = read_force(board, pin=0)  # Read force sensor value from analog pin 0
```

#### Function:
- `read_force(board, pin)`: Reads the force sensor value from the specified analog pin.

---

### 7. `location.py`
**Description:** This module keeps track of the current position of the rover and its projected destination.

#### `Rover` Class
**Usage:**
```python
from location import Rover

# Example usage
rover = Rover(initial_x=0, initial_y=0, initial_heading=0)
rover.move(distance=10, angle=45)  # Move 10 units at a 45-degree angle
rover.update_heading(90)  # Update heading to 90 degrees
position, heading = rover.locate()  # Get current position and heading
```

- `move(distance, angle)`: Updates the position based on distance moved and angle turned.
- `update_heading(new_heading)`: Updates the rover’s heading in degrees.
- `locate()`: Returns the current position and heading of the rover.

---

### 8. `mpu.py`
**Description:** This module interfaces with an MPU6050 sensor to retrieve acceleration, gyroscopic, and temperature data.

#### `MPU` Class
**Usage:**
```python
from mpu import MPU

mpu_sensor = MPU()
data = mpu_sensor.readmpu()
print(data)  # Prints acceleration, gyro, and temperature readings
```

- `readmpu()`: Continuously reads and returns acceleration, gyroscopic, and temperature data.

---

### 9. `nrf.py`
**Description:** This module provides functionality for wireless communication using the nRF24L01 transceiver module.

#### Usage:
```python
from nrf import master, slave

# Example usage
master(count=5)  # Send 5 transmissions
slave(timeout=6)  # Listen for incoming transmissions for 6 seconds
```

#### Functions:
- `master(count)`: Sends `count` float values incrementally via nRF24L01.
- `slave(timeout)`: Listens for incoming transmissions and prints received float values.

---

