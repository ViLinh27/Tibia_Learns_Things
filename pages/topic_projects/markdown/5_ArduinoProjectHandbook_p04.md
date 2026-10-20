# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 4:Disco Strobe Light</u>

- Page 61 of the book

### **GOAL** : Apply skills learned in Project 3 to make strobe light with **adjustable** speed settings

### Supplies

- Arduino Board
- Breadboard
- Jumper Wires
- 2 blue LEDs
- 2 red LEDs
- 50K-ohm Potentiometer
- 4 220-ohm resistors

### How it Works

- turn potentiometer up / down changes speed of flashing lights (strobe effect)
- Figure 4-1 shows red and blue lights to make strobe kinda like a police light
  - ![police light example from book](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528602/figure4-1.jpg)
- make sure to connect LEDs of same colour to same arduino pins so they light together
- can add up to 10 LEDs, just update sketch to include your ouput pins and new number of LEDs

### The Build

- ![book setup to show how to connect 2 LEDs together](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528602/figure4-2.jpg)
- | LEDs                | Arduino |
  | ------------------- | ------- |
  | Negative Legs       | GND     |
  | Positive Leg (red)  | Pin 12  |
  | Positive Leg (blue) | Pin 11  |

- | Potentiometer | Arduino |
  | ------------- | ------- |
  | Left pin      | GND     |
  | Center Pin    | A0      |
  | Right Pin     | +5V     |

- Example from book:
  - ![ Book Example set up](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528603/figure4-3.jpg)
- My setup:
  - ![Hardware setup 01](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528607/proj04_mysetup.jpg)

### The Sketch

- Code sets pu analog signal from potentiometer to arduino as input and pins connected to LEDs as output
- arduino reads analog input from potentiometer and uses THIS VALUE (analog input) as DELAY VALUE
  - delay val: amount of time that passes before LEDs change state (either on or off)
- Meaning LEDs are on and off for duration of POTENTIOMETER VALUE
  - changing potentiometer value alters speed of flashing
- sketch cycles through LEDs to make strobe effect
- Book reference code
  - ![book reference code](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528605/proj04_bookCode.jpg)
- My code (I just have to copy from the book)
  - ![code setup 01](https://res.cloudinary.com/wjd2npkc/image/upload/v1792528606/proj04_mycode.jpg)

### Simulation 01

- looks successful
- The potentiometer does affect the speed at how the lights change
- Looks like I should stick to avoiding putting anything directly on the horizontal GND/ Postive rails on either end of the breadboards
  - In this case LEDs
