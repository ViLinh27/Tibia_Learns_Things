# Complete Electronics Self-Teaching Guide with Projects

## 1: **DC Review and Pre-Test**

- Review basics of elecricity like DC (direct current) to make sure you know essentials

### In this chapter:

- current flow
- potential or voltage difference
- ohm's law
- resistors in series and parallel
- power
- small currents
- resistance graphs
- Kirchhoff's Voltage Law
- Kirchhoff's Current Law
- Volrage and current dividers
- Switches
- Capacitor charging and discharging
- Capacitor in series and parallel

### Current Flow

- Electrical and electronic devices work because of an electric current

---

- Q1: <u>What is an electric current?:</u>
  - My answer:
    - flow of electrons in a circuit basically
  - Book Answer:
    <details> <summary> Click to Reveal</summary>
        <ul> 
          <li>electric current is flow of electric charge</li>
          <li>The electric charge usually consists of negatively charged electrons</li>
          <li>However, in semiconductors, there are also positive charge carriers called **<u>holes</u>**.</li>
        </ul>
      </details>
  - What I learned here:
    - I need to be more detailed in my answers
    - It helps to know the specifics like the charges and outlier possibilities like semiconductors

---

- Q2: <u>There are several methods that can be used to generate an electric current. Write at least 3 ways an electron flow ( or current ) can be generated.</u>
  - My answer:
    - A standard electric circuit like with a basic PCB and a bunch of wires
      - electrons are moving through wires here
    - Incandescent light bulbs
      - ordinary conductor
      - causes Joule heating
    - in a semiconductor
      - although the charge can be positive here (electroncs are negative)
  - Book Answer:
    <details> <summary> Click to Reveal</summary>
    (These are the most common ways to generate current)
    <ul>
      <li>
       <u>Magnetically</u>: 
         <ul>
           <li> includes induction of electrons in a wire rotating in a magnetic field</li>
           <li>example: generators turned by water, wind or steam, or fan belt in car</li>
         </ul>
      </li>
      <li>
       <u>Chemically</u>:
         involves <u>electrochemical generation</u> of electrons by reactions between chemicals and electrodes (as in batteries)
      </li>
      <li>
        <u>Photovoltaic generation of electrons</u>:
          occurs when light strikes semiconductor crystals (solar cells).
      </li>
    </ul>
    <br>
    (Less common ways to generate electric current:)
    <ul>
      <li>
        <u>Thermal Generation</u>:
        <ul>
          <li>uses temperature differences between thermocouple junctions</li>
          <li>Used in generators on spacecrafts fuled by radioactive material</li>
        </ul>
      </li>
       <li>
        <u>Electrochemical reaction</u>:
        occurs between hydrogen, oxygen, and electrodes (fuel cells)
      </li>
      <li>
        <u>Piezoelectrical</u>:
        <ul>
            <li>involves mechanical deformation of **piezoelectric substances**</li>
            <li>example: piezoelectric material in heels of shoes power LEDs that light up when you walk</li>
        </ul>
      </li>
    </ul>
    </details>

  - What I learned here:
    - I misunderstood the question for one.
    - I was thinking too detailed and understood the question as " give me situations that can make electrons flow only".
      - I didn't consider the effects beyond that
    - I didn't consider the fact that (for example) electric currents make magnetic fields, this means the electric current can be created **magnetically**.
      - This was mentioned in the Wikipedia article.
    - I was thinking of different real world examples of electric currents but the definition I had in my head was too narrow.

---

- Q3:
  - Context:
    - Most simple examples in this book contain a battery as voltage source
      - batteries provide potential difference to circuit that enables current to flow (here)
      - electrons are electric charge, that flow from terminal with **excess number** of electrons to terminal with **deficiency** of electrons
      - this flow happens in **any complete circuit** connected to battery terminals
      - **this difference** is what makes **potential difference** in batteries
        - electrons try to balance said difference
    - <u>electron flow</u>
      - electrons have - charge so flow from - to +
    - current flow
      - - to - flow
      - aka conventional current flow
    - many semiconductor devices have symbol that contains arrowhead pointing in direction of conventional current flow
  ***
  - 3A: <u> Draw arrows to show the current flow in Figure 1.1. The symbol for the battery shows its polarity</u>
    - My Answer on figure 1.1:
      - ![Figure 1.1 with my arrows](https://res.cloudinary.com/wjd2npkc/image/upload/v1792771088/figure1-1.jpg)
  ***
  - 3B: <u> What indicatesd that a potential difference is present?</u>
  - My Answer:
    - There's a battery that causes electrons to flow
    - There's a positive and negative terminal for the electrons to flow in a direction
    - So there's a potential difference
  ***
  - 3C: <u> What does the potential difference cause? </u>
  - My answer:
    - The - charged electrons will flow towards the positive terminal because there's an excess of electrons at the negative termminal and a deficiecy at hte positive terminal
  ***
  - 3D: <u> What will happen if the battery is reversed </u>
  - My answer:
    - The current flow will be reversed
  ***
  - Book Answer:
      <details> 
      <summary> Click to Reveal</summary>
      <ul>
          <li>3A: <img src="https://res.cloudinary.com/wjd2npkc/image/upload/v1792771088/figure1-2.jpg" alt="figure 1.2, answer to Q3 A"/></li>
          <li>3B: The battery symbol indicates that a difference of potential <u>(aka voltage)</u> is being supplied to the circuit</li>
          <li>3C: Voltage causes current to flow if there is a complete circuit present, as shown in figure 1.1</li>
          <li>3D: The current flows in the opposite direction</li>
      </ul>
      </details>
  - What did I learn?
    - 3A:
      - I got the terminology mixed up from the looks of it.
      - THe question was asking for current flow.
        - On the libreText physics site, the text talked about common misconceptions of only talking about the flow of + charges, when electrons have a - charge.
        - I forgot that the text also mentions that it's convention to talk about + charge when talking about current direction. THe conventional current if you will.
    - 3B:
      - I took the question metaphorically concerning the shown circuit schematic.
      - Since the diagram in figure 1.1 represents a circuit I thought the question was asking " What is the thing in this circuit that makes the potential difference here."
      - I didn't think the question was that literal, as in the battery symbol is what shows the fact there's potential difference here.
    - 3C:
      - Aside from the direction being (conventionally) wrong, I'm not completely wrong in this answer.
      - This question is just broad so I was thinking too much into the question so my answer is too specific.
      - The potential difference just makes the current flow
    - 3D:
      - Since a battery has a + terminal and a - terminal, it made sense that if the battery got reversed, the current flow would too
      - Since the voltage comes from the battery here to my understanding

### Ohm's Law

- Q4:
  - Context: Ohm's Law states the fundamental relationship between voltage (V), current (I), and resistance (R)
  - <u>What is the algebraic formula for Ohm's Law?</u>
  - My answer
    - V = I x R
    - Voltage = current (intensity) x Resistance
  - Book answer
    <details> 
      <summary> Click to Reveal</summary>
      <ul>
          <li>V = I x R</li>
          <li>This is the most basic equation in electricity, and you should know it well. Some electronics books state OHm's law as E = IR. E and V are both symbols for voltage. This book uses V to indicate voltage. When V is used after a number in equations and circuit diagrams, it represents **volts**, the unit of measurement of voltage.  Also, in this formula, resistance is the opposition to current flow. Larger resistanc ersults in smaller current for any given voltage.</li>
      </ul>
    </details>
  - What did I learn?
  - I know this fundamental so that's good.
  - It helps to picture the Ohm's law formula in a pyramid like so:
    - ![Ohm's law pyramid](https://res.cloudinary.com/wjd2npkc/image/upload/v1792771087/ohm-pyramid.jpg)
      - figure above from this [link](https://developer.wildernesslabs.co/Hardware/Reference/Equations_and_Laws/Voltage/Ohms_Law/)

---

- Q5: Use Ohm's law to find the answers in this problem
  - 5A:
  ***
  - 5B:
  ***
  - 5C:
  ***
  - 5D:
  ***
  - Book Answer
  - What I learned

### Resistors in Series

### Resistors in Parallel

### Power

### Small Currents

### The Graph of Resistance

### The Voltage Divider

### The Current Divider

### Switches

### Capacitors in a DC Circuit

### Summary

### DC Pre-Test
