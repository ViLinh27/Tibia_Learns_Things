# Arduino Project Handbook

25 Practical Projects to get you started by Mark Geddes

## **Part 1: LEDS**

## <u>Project 5: Plant Monitor</u>

- Page 45 of the book

### **GOAL** : Learn new type of **analog sensor** that <u>detects moisture levels</u>. Set up light and sound alarm system to tell you when your plant needs watering.

### Supplies

- arduino board
- jumper wires
- LED
- HL-69 hygrometer soil moisture sensor
- Piezo buzzer

### How it Works

- THe prongs of the moisture sensor detects mositure level in surrounding soil by passing current through soil and measure resistance
- Damp soil conducts electrictity easily
  - less resistance
- Dry soil conducts poorly
  - higher resistance
- The parts of the sensor (figure 5-1)
  - actual prog sensor(a)
    - 2 pins on sensor need to connect to 2 separate pins on controller
      - connecting wires usually supplied
  - controller (b)
    - other side of controller has 4 pins
    - 3 of which connect to arduino
    - 4 pins from left to right
      - AO (analog out)
      - Do (digital out)
      - VCC (figure 5-2)
      - we can read values from controller through IDE when it's connected to computer

- Reference photo 5-1
  - ![reference photo]()
- Reference photo 5-2
  - ![reference photo]()

- lower readings: more moisture detected
- higher readings: dry
  - reading > 900
    - is your plant still alive
  - LED will light and buzzer will sound

### The Build

- | Sensor Controller | Arduino  |
  | ----------------- | -------- |
  | VCC               | +5V      |
  | GND               | GND      |
  | AO                | A0       |
  | DO                | Not used |

- | LED          | Arduino |
  | ------------ | ------- |
  | Positive leg | Pin 13  |
  | Negative leg | GND     |

- Reference photo 5-3
  - ![reference photo]()

- Reference photo 5-4
  - ![reference photo]()

- - Reference photo 5-5
  - ![reference photo]()

- My hardware setup before looking at the reference photo
  - ![my hardware setup 01]()

- My hardware setup after looking at the reference photo
  - ![my hardware setup 01-1]()
- - Reference photo 5-6
  - ![reference photo]()
- The hardware in tinkercad is kind of different.
  - The sensor isn't the 2 part one like in the book (the one with a separate sensor and controller).
  - It looks like during the simulation I can manually set the sensor to wet or dry to mess with what is going into the rest of the parts.
  - I don't expect this first simulation to work because of the differing parts
  - Not sure if the sensor in tinkercad has a potentiometer I can calibrate the plant monitor with.

- - Reference photo 5-6 with the potentiometer on controller thing
  - ![reference photo]()

### The Sketch

- what does it do
  - defines arduino pin A0 so it reads nmoisture sensor value
  - defines arduino pin 11 as output for buzzer
  - define pin 13 as output for LED
  - Serial.Println() function sends reading from sensor to IDE
    - we see value on screen this way
  - change vlaue in this line `if(analogRead(O) > 900){` depending on reading from sensor when dry
- My code (copied from book)
  - ![my code 01]()
- The sensor was not calibrated yet

### Simulation 01
