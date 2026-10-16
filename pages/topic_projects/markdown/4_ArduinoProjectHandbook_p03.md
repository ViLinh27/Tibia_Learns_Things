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
- ![hardware set up 01]()

### The Sketch

- My first code set up:
- ![code setup 01]()

#### What does the book code do

1. Reads input from potentiometer
2. maps input value to output range

- meaning the LEDs

3. for loop over all outputs

- If output num of LED in series < mapped input range then LED turns on
- if NOT that, then LED turns off
- syntax of map() in arduino c++:
  - map(1,2,3,4,5)
  - 1: input var
  - 2: lower bound of current range
  - 3: upper bound of current range
  - 4: lower bound of target range
  - 5: upper bound of target range

#### How to get the simulation to work

- turn potentiometer to the right LED lights up in sequence
- turn it left, they turn off in sequence

#### Simulation 01

- Failure
- I know the setup you have doesn't have to be accurate to the book, but I still think I didn't connect the hardware correctly.
- Comparisons between book diagram and my current setup
  - The resistor legs connected to +5v aren't directly on the +5v rail on the one side of the breadboard in the diagram compared to my setup
    - I tried connecting the positive legs of the LEDS directly
  - The book setedup takes advatage of how the middle holes of the breadboard are all vertically connected compared to mine (that is if the 2 GND and +5f rails are going horizontally).
  - There's no wire crossing in the book diagram compared to mine
  - The book diagram takes full advantage of the +5v and GND rails on both sides of the breadboard compared to mine
  - Still not sure if using the same holes in a circuit for several jumper wires is a bad idea or not though but I have that in my setup while the book one doesn't so should probably avoid that in the future

#### Simulation 2

- My second set up:
- ![hardware set up 02]()
- My second code set up:
- ![code setup 02]()
- I realize I never connected the +5v rail connected to the LEDs back to the arduino in teh first simulation. No wonder it wasn't working before (simulation 1) but it's still not working here
- I also didn't use the resitors to bridge the gap in holes in the breadboard like what the book suggested
- Potential reasons I could not be doing this corrctly
  - I didn't connect the potentiomter to ground correctly
  - I'm mixing up th wiring to the ground rail for both the LEDs and the potentiomter
  - I'm still not bridging the circuit between the breadboard's trench that well.
- I'll have to go even closer to the book diagram now for how to set up my circuit. Oh well

#### Simulation 3

- My third set up:
- ![hardware set up 03]()
- My third code set up:
- ![code setup 03]()
- This simulation was a failure
- I didn't notice that in the book that the columns in the breadboard are sepearte between the anode and cathod of the leds (as in the led legs are using different columns)
  - in my current set up (#3), I have each led leg use the same set up. It could be why it's not turning on because the negative an dpositive are going in together in one column, so I'm mad at myself for that.
-

#### Simulation 4
