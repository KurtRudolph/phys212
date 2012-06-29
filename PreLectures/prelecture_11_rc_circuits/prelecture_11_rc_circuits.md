# RC Circuits

## Overview
* Last time
  * Kirchhoff's Rules
      * Voltage Rule \[\sum \Delta V_n = 0\]
      * Current Rule \[\sum I_{in} = \sum I_{out}\]
  * Real Batteries
      * \[V_b = V_0 \frac{ \frac{ R}{ r}}{ 1 + \frac{ R}{ r}\]
* Today we discuss _RC Circuits_
    * [[/images/rc_circuit.png]] 
    * Start with a circuit that charges a battery through a resistor.
    * Move on to a circuit that removes the battery so the capcitor is
      discharged.
    * Close by discussing the energy flow in these circuits.

## Charging Capacitor: Qualitative Description
* Simple circuit containign a battery, capacitor and resistor.
* We saw last time in the circuit with just a battery and a capacitor that
  * \[V_b = V_c\]
  * \[q = C V_C\]
  * [[capcitor_only.png]]
  * This was viewed as being charged instantaniously after the battery was connected to it.
* We now look at adding a resistor to the circuit.
  * [[qualitative_circuit.png]]
  * This will limit the rate at which charge will flow to the capacitor and hence the 
    rate at which the voltage accross the capacitor is able to be charged.
  * We now close the gate and charge begins to flow
      * [[capcitor_and_resistor_t0.png]]