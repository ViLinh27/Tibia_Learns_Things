# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## Project 0: Getting Started

Preliminary notes before we begin the project

### Hardware

#### Arduino Uno

- What this book will use
- Open source
- Elements
  1. Reset button USB chip
  2. 14 digital in/out pins (0-13)
  3. Surface mount pin 13 LED
  4. TX/RX LEDs
  5. ICSP Header ATMEGA328P Controller
  6. 6 analog in pins (0-5)
  7. Power pins
  8. Power sockket 2.1 mm tip 9 volts
  9. Usb socket

#### Power

- Connect to USB on computer first
- When not computer connected, can run with 9-volt AC adapter / 9-volt battery pack with 2.1mm jack
  - Center pin connected to positive wire

#### Breadboards

- No soldering in this book, just plugging in stuff thanks to breadboard

- Come in a lot of sizes

- Note that +5V and –Gnd are on both sides of breadboard (in this book)

- Main boards has 30 columns of tie points connected vertically

- Blue and red lines at top and bottom are power rails that we use to power components inserted into main breadboard

#### Jumper Wires

- Make connections to breadboards
- Insert jumper wire into breadboard hole => held in place beneath board with spring clip => This makes the electrical connection
  - Place component in hole next to that hole to create circuit

### Programming the Arduino

#### Download the ide here

- www.arduino.cc

#### IDE interface

- Doesn't look too different from usual IDEs
- Sketch is where you put your code
- Toolbar buttons:
  - Verify
  - Upload
  - New sketch
  - Open sketch
  - Save sketch
  - Serial output

#### Arduino Sketches

- What we call the program parts of each projectg
- Strict instructions like all programs

#### Libraries

- Listed like this in the sketch:
  `#include <Servo.h>`
  - Looks like C
- Make sure to install them first before using in sketch (duh)

### Testing your Arduino Blinking LED

#### Make sure arduino is working correctly

- Arduiono can only hold one sketch at a time (remember)
- Sketch will run each time arduino is turned on until new sketch uploaded

#### GOAL: turn on LED for 1 sec, then off for 1 sec repeatedly

- LED emits light when current passed through
- Current flow in one direection
- Longer wire must connect to positive power connection
  - the bent part on the light
- LED needs current limiting resistor, so it doesn’t burn out
  - Built in resistor inline with pin 13 of Arduino

#### **<u>THE TEST : DONE IN TINKERCAD</u>**

- Also used this link for reference:
  - [Resource document that explains this project in tinkercad context](https://resources.finalsite.net/images/v1722986196/brightonk12com/nbvvlmvtlqnocvshevwm/01tinkercadandarduinobasics.pdf)
- I started off putting a wire between the top left hole on the breadboard (-) and the d12 hole on the arduino because 13 and ground had an led connected to it
  - When i test the simulation I get what looks like an error:
    - Current through the LED is 52.5 mA, while recommended maximum is 20.0 mA. The usable lifetime of hte LED may be reduced.
  - Looks like the too much power going through to the LED.
- I used the arrangement with the breadboard from the resources file at first. This puts the led in the breadboard, and the resistor in the breadboard. Some wires connect from the breadboard to the arduino.
  - With the code from the book, there seems to be an issue.
  - Code:
    1. test
