# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 2: Light Dimmer</u>

### **GOAL** : Create dimmer switch by adding potentiometer to control brightness of an LED

### Supplies

- (still doing this in tinkercad)
- Arduino board
- Breadboard jumper wires
- LED
- 50K- ohm potentiomter
- 470- ohm resistor

### What's a potentiometer

- Resistor that has a knob that lets us vary resistence of said potentiometer when turning it.
- Think a volume button (commone one)
- If you're using actual equipment, you'll need a 50K-ohm potentiomter for this project.

### How it works

- The potentiomter is messing with an **analog signal**.
  - analog signal is the physical measurement of what's going on
  - analog means **continous stream of info** coming in
    - kinda like how humans perceive things
- digital info has to **estimate** analog data using numbers
  - THe way the arduino does it from teh potentiomter is through the **voltages**
  - A0 to A5 pins in arduino
- **Persistence of vision**
  - When the LED is being messed with in this project, it's actually constantly being turned on
    and off but we can't see that switch since it's so fast
  - **Pulse width modulation (PWM)**
    - What's basically happening (considering the LED thing mentioned above) is that pulse the arduino creates is being measured in its duration of said pulse (the on and off switching).
    - The duration of that pulsing is the **pulse width**
    - The pulse duration cycle is what the potentiometer is measuing
      - THe average output of said pulses
- Varying the pulse cycles can give voltages that are full at 5 volts or off (which is 0 volts).
- So we can chagne the voltage being sent to the LED and make it dimmer and brighter to match analog signal from potentiomter.
- <u>Only pins 3,5,6,9,10 or 11 on arduino can use PWM</u>
- Figure 2-1 on p31 of book gives example of how pwm looks as wave form

### **<u>THE BUILD : DONE IN TINKERCAD</u>**

#### Try 1

- The steps:
  1. Potentiometer goes somwhere on breadboard
  2. Center pin of potentiometer gets connected to A0 on Arduino
  3. one of the outer pins get connnected to +5V rail on breadboard (that's the red positive line)
  4. THe other outer pin of potentiometer gets connected to GND on breadboard
  - | potentiomter | Arduino |
    | ------------ | ------- |
    | left pin     | +5v     |
    | center pin   | A0      |
    | right pin    | GND     |
  5. insert LED into breadboard
  6. attach positive leg (longer) to pin 9 of arduino (via 470-ohm resistor)
  7. attach negative leg to GND
  - | LED          | Arduino                  |
    | ------------ | ------------------------ |
    | positive leg | pin 9                    |
    | negative leg | GND via 470-ohm resistor |
  - There's a diagram of what the setup is supposed to look like on p 32 of the book (figure 2-3)
  8. Upload the code in sketch section from book
  9. Turn potentiometer to control brightness of LED
  - If you're also doing this in tinkercad, you have to turn on "start simulation " button before doing this

- My first setup:
  - ![first setup project 2](https://res.cloudinary.com/wjd2npkc/image/upload/v1791580132/proj2-1st-setup.jpg)
  - ![ First code from sketch section project 2](https://res.cloudinary.com/wjd2npkc/image/upload/v1791585110/proj2-1st-code.jpg)
- ##### potential uses for potiometer circuit shown in this project
  - cluster LEDs together to create adjustable flashlight
  - night light
  - display case light
  - anything that uses dimming lights

##### The Sketch

###### How this sketch works

- set up pin A0 as potentiometer, pin 9 as OUTPUT to power LED
- run loop that **continuously** reads value from potentiometer, sends value as voltage to LED
- voltage value between 0-5 volts
  - brightness of LED based on that

##### Was this try successful?

- NO

###### Why do i think so?

- I don't think I connectedd the LED correctly
  - I connected the positive leg of hte LED to the +5v rail (via resistor) then that goes to pin 9
  - The book says that leg goes directly to pin 9
- The negative leg of the LED also goes through the GND rail of the breadboard
- in my head because it's a horizontal connection on the rails, it should have worked, but i guess not

#### Try 2

- I setup the components closer to figure 2-3 on p32 of the book:
- ![Second setup project 2](https://res.cloudinary.com/wjd2npkc/image/upload/v1791587969/proj2-2nd-setup.jpg)
  - Looks like another issue I had was the fact that the resistor is only set up for the positive charge with the LED, I put it on both before
  - Embarassingly, I was also missing a connection from one of the +5V rails to the 5V pin on the arduino (to my understanding)
    - This was the positive connection on the potentiometer to the arduino by the way (that I was missing)
  - This setup isn't exactly like the book but gets all the essentials down.
- The code remains the same
- ![Code from before](https://res.cloudinary.com/wjd2npkc/image/upload/v1791587969/proj2-2nd-code.jpg)
  - all I added was an extra comment
- I fixed the errors mentioned above, and **this attempt was a success**. Yay.
