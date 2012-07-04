# Homework: Electric Current

## Circuit 1 with Resistor and a Battery

A circuit is constructed with five resistors and a battery as shown. 
The battery voltage is \[V = 12.0 V\]. The values for the resistors 
are: \[R_1 = 75.0 \Omega\], \[R_2 = 118.0 \Omega\], \[R_3 = 147.0 \Omega\]
and \[R_4 = 61.0 \Omega\].

The value for \[R_X\] is unknown, but it is known that \[I_4\], 
the current that flows through resistor \[R_4\], is zero.

[[circuit_1.png]]

Let
* \[V_b = 12.0 V\]
* \[R_1 = 75.0 \Omega\] 
* \[R_2 = 118.0 \Omega\] 
* \[R_3 = 147.0 \Omega\]
* \[R_4 = 61.0 \Omega\]. 
* \[I_4 = 0\]

### 1)
What is \[I_1\], the magnitude of the current that flows through the resistor \[R_1\]?

* \[I_1 = \frac{ V_b}{ R_1 + R_3}\]
  * Correct

* \[\frac{ v}{ R_1}\]
  * It looks like you have calculated the current assuming that 
    the voltage across \[R_1\] is the battery voltage, which it 
    is not. The current does not return directly to the battery 
    after leaving \[R_1\]. Where does it go before returning to 
    the battery?

### 2)
What is \[V_2\], the magnitude of the voltage across the resistor \[R_2\]?

* \[V_2 = V_b - I_1 R_3\]
  * Since \[I_4 = 0\] we are able to say \[V_1 = V_2\].
  * \[V_b = R_1 I_{1,2} + R_2 I_{1,2}\]
  * \[v_{drop} = I_1 R_1\]
  * \[R_{equiv} = \left(\frac{ 1}{ R_1 + R_3} + \frac{ 1}{ R_2 + R_x}\right)^{-1}\]
  * \[ \]
  * \[I_2 = \frac{ V_b}{ R_2 + R_x}\]

* \[0\]
  * The voltage across \[R_2\] is not equal to zero since the current 
    through \[R_2\] is not zero. Look at the circuit closely to determine 
    how the voltage acrosss and current through \[R_1\] are related to 
    the same quantities for \[R_2\].
* \[12V\]
  * The voltage across \[R_2\] is not equal to the battery voltage. Think 
    about the voltage across \[R_4\]. What does that tell you about \[V_1\] and 
    \[V_2\]?

### 3)
What is \[I_2\], the magnitude of the current that flows through the resistor \[R_2\]?

* \[I_2 = \frac{ V_2}{ R_2}\]
