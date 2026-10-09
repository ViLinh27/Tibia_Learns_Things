# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 2: Light Dimmer</u>

### **GOAL** : Crate dimmer switch by adding potentiometer to control brightness of an LED

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

-
