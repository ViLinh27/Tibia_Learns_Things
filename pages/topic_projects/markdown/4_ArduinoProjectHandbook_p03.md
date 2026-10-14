# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 3: Bar Graph</u>

### **GOAL** : Combine what we've learned in previous led projects to create led bar graph that we can control with a potentiometer

### Supplies

- Arduino Board
- Breadboard
- Jumper wires
- 9 LEDs
- 50K- ohm potentiometer
- 9 220-ohm resistors

### How it works

- The LEDs are lined up and get an analog signal to either turn on one-by-one or turn off one-by-one
- Here the analog signal is the potentiometer
  - we turn it one way to turn on in sequence
  - we turn it other way to turn off in sequence
- Turning on lights one at a time:
  - ![Figure 3-1 Lights turn on one at a time](https://res.cloudinary.com/wjd2npkc/image/upload/v1792003810/figure3-1_A.jpg)
- Lights are all on:
  - ![Figure 3-1 Lights are all on](https://res.cloudinary.com/wjd2npkc/image/upload/v1792003810/figure3-1_B.jpg)
- Lights turn off in sequence
  - ![FIgure 3-1 Lights turn off in sequence](https://res.cloudinary.com/wjd2npkc/image/upload/v1792003810/figure3-1_C.jpg)

### The Build

| LEDs          | Arduino                        |
| ------------- | ------------------------------ |
| Positive Legs | Pins 2-10 via 220-ohm resistor |
| Negative legs | GND                            |

| potentiometer | arduino |
| ------------- | ------- |
| Left pin      | GND     |
| center pin    | A0      |
| right pin     | +5V     |

- My first set up:
- ![]()

### The Sketch

- My first code set up:
- ![]()

#### What does the book code do

1. Reads input from potentiometer
2. maps input value to output range

- meaning the LEDs

3. for loop over all outputs

- If output num of LED in series < mapped input range then LED turns on
- if NOT that, then LED turns off

#### How to get the simulation to work

- turn potentiometer to the right LED lights up in sequence
- turn it left, they turn off in sequence
