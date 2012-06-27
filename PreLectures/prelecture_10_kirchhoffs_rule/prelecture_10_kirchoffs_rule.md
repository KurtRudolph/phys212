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


