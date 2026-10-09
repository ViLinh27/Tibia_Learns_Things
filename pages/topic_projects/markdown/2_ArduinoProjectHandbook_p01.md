# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 1: Pushbutton-controlled LED</u>

### **GOAL** : Adding a pushbutton switch to led circuit to control when led is lit

### Supplies

- (important note: I'll be doing this in tinkercad but it helps to know the supplies)
- Arduino board
- Breadboard
- Jumper wires
- Led
- Momentary tactile four-pin pushbutton
- Lots of switches exist,this is just one of them
- 10k ohm resistor
- 220 ohm resistor

### How it works

- Button press => pushbutton complets circuit => light turns on
- Button not pressed anymore => connection spring backs and breaks circuit => light turns off
  - Note: pushbutton aka MOMENTARY/ NORMALLY OPEN switch
    - TOGGLE SWITCH is like a light switch, it stays on until switched off again and vise versa
- Pushbutton has 4 pins
  - For this we only need 2 at a time for connection to work
  - P24 has a figture 1-2 that illustrates how the pins connect for form circuit
- #### **<u>THE BUILD: DONE IN TINKERCAD</u>**
  - ##### Try 1
    - This is what the sedt up looks like going through the first set of instructions before the set up diagram (figure 1-4 on p26 of book)
    - ![Set up 01 Proj 1](https://res.cloudinary.com/wjd2npkc/image/upload/v1791573713/00-setup01.png)
    - This is what the actual setup diagram looks like (in tinkercad):
    - ![Set up 02 Proj 1](https://res.cloudinary.com/wjd2npkc/image/upload/v1791573714/01-setup02.png)
    - The setup above didn't work when simulation started ( I added in code from book)
      - code used below (public domain):
      - ![Code 1 Proj 1](https://res.cloudinary.com/wjd2npkc/image/upload/v1791573713/02-code1.png)
      - I think I'm not using the resistors correctly because it looks like the bulb burnt out during the simulation
      - it's possible i didn't do the setup correctly according to the book too
  - ##### Try 2
    - I changed the steup I had from above a bit to match the book more. This is what I have:
    - ![Setup 03 Proj 1](https://res.cloudinary.com/wjd2npkc/image/upload/v1791573714/03-setup03.png)
    - The code is the same
    - ![Code 02 Proj 1](https://res.cloudinary.com/wjd2npkc/image/upload/v1791573713/04-code02.png)
    - **The simulation was a success**
    - Looks like the main issue is I wasn't connecting the LED correctly. I had the positive node directly into the 5V band on the breadboard instead of going through the resistor.
    - Which does explain the burnt out bulb and too much electricity going to it to begin with.