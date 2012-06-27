# Kirchhoff's Rules

## Overview
* Start with a brief overview of the devices we will using
  * Switch
      * [[switch.png]]
  * Battery
      * [[battery.png]]
  * Capacitor
      * [[capacitor.png]]
  * Resistor
      * [[resistor.png]]
* Then we will introduce _Kirchoff's Rule_
  * \[\sum \Delta V_n = 0\]
      * any closed loop
  * \[\sum I_in = \sum I_out\]
      * at any node
* Close by modeling a real battery as an ideal battery in series

## Review of Electrical Devices
* Battery
  * Maintain a constant potential difference across their terminals
      * sometimes this potential difference is referred to as the EMF
      * \[EMF \equiv \varepsilon = V_b\]
  * [[battery.png]]
* Capacitors
  * Capacitors store charge
  * \[V_C = \frac{ Q}{ C}\]
      * the voltage drop accross capacitors is equal to excess charge
        \[Q\] on one plate divided by \[C\] it's capacitance.
      * We speak about capacitors in terms of the rate of change
        across it's plates.
  * [[capacitor.png]]
* Resistors
  * The voltage drop across resistors is proportional to current that
    flows through it.
  * \[V_R = I R\]
  * [[resistor.png]]
* Switch
  * Used to add or remove other devices from the circuit.
      * When the switch is open no current passes through it
        when the switch is close current passes freely through it.
        and the voltage across the switch is zero.
  * [[switch.png]]

## Kirchoff's Rules
* Voltage Rule
  * \[\sum \Delta V_n = 0\]
  * If you start on any point in a circuit and follow that 
    around a complete loop the net change in the electric potential
    is zero.
  * [[circuit_loop.png]]
* Current Rule
  * \[\sum I_{in} = \sum I_{out}\]
  * Essentially a statement of charge conservation, at any node in
    a circuit a place where two or more wires meet, the sum of the
    currents flowing in is equal to the sum of the currents flowing out.
  * [[circuit_node.png]]

## Conventions
* In order to apply these two rules to circuits we must first address 
  the issue of sign convention.  In particular we need to address the
  conventions for the direction of current flow and the sign in which
  the voltage changes.
* One loop circuit
  * [[one_loop_circuit.png]]
  * It doesn't matter which way you go ultimately the change in
    potential is zero.
  * For historical reason we will go clockwise around the loop
  * we define \[\Deslta V_{R_1} = + V_{R_1}\] to be positive across resistors.
  
## Single Loop Example
* Again looking at a single loop
  * [[one_loop_circuit.png]]
  * As we move around the loop from point a to point b 
    we encounter a voltage drop.  Which is equal to the 
    product of the current and the resistance.
      * \[\Delta V_{R_1} = + I R_1\]
      * \[\Delta V_{R_2} = + I R_2\]
      * \[\DELTA V_{batter} = - V_b\]
      * Hence \[\sum \Delta V_n = I R_1 + I R_2 + (- V_b) = 0\]
      * As expected we find that \[I = \frac{ V_b}{ R_1 + R_2}\]
            * This follows that the direction is clockwise.

## Two loop example
* We now look at a two loop example. 
  * [[two_loop_circuit.png]]
  * Analyzing the loops we find three equations and three unknowns.
      * \[I_1 + I_2 = I 3\] kirchoff's current rule
      * \[I_3 R_3 + V_2 + I_1 R_1 - V_1 = 0\] outer loop
      * \[-I_2 R_2 + I_1 R_1 - V_1 = 0\]
      * [[two_loop_circuit_1.png]]

## Question 1
Consider the circuit shown above. Which of the following statements 
best describes the current flowing in the blue wire connecting 
points \[a\] and \[b\].

[[q1.png]]

* No current flows between \[a\] and \[b\]
  * Because the halves of the circuit above and below the blue wire 
    are identical, the voltage at \[a\] (and hence also at \[b\]) is 
    just half the voltage of the battery. This means that the current 
    in the upper resistor labeled R is the same as the current in the 
    lower resistor labeled \[R\], which by Kirchhoff's Current Rule 
    tells us that the current in the blue wire it self must be zero. 
    Exactly the same argument can be made at point \[b\].

## Real Batteries
* Thus for we have considered batteries to be ideal, i.e. we have assumed
  that batteries produce a constant potential difference across their
  terminals independent of the current being drawn.
* Now we will consider real batteries where the voltage across the terminals
  can decrease if a large enough current is being drawn from the battery.
* Example
  * [[battery_and_current.png]]
  * \[I = \frac{ V_0}{ R + r} \]
      * EMF of the battery divided by the total resistance.
  * In turn the voltage which appears at the terminals is as follows
      * \[V_b = V_0 - I r\]
      * \[V_b = V_0 - \frac{ V_0 r}{ R + r}\]
      * \[V_b = V_0 \frac{ \frac{ R}{ r}}{ 1 + \frac{ R}{ r}}\]


## Question 2
The 'real' batteries and the resistors in both cases illustrated above 
are identical. In which case is the voltage across the terminals of 
the battery closest to the ideal battery voltage \[V_0\]?
[[q2.png]]

*  The voltage across the terminals of the battery is closest to ideal in _Case A_
  * The current supplied by the battery in _Case A_ is smaller than in _Case B_ 
    since the resistance of the external load in _Case A_ is twice as big as in 
    _Case B_. If the current supplied by the battery is smaller, the voltage drop 
    across the internal resistance of the battery will also be smaller, and hence 
    the voltage across the terminals of the battery will be closer to the ideal 
    battery voltage.