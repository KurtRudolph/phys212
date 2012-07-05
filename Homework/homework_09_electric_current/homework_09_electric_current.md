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

### 4)
What is \[R_X\], the value of the unknown resistor \[R_X\]?

* \[R_X = \frac{ I_1 R_3}{ I_1}\]

### 5)
What is \[V_1\], the magnitude of the voltage across the resistor \[R_1\]?

* \[V_1 = V_2\]
  * Since \[I_4 = 0\] we are able to say \[V_1 = V_2\].

### 6)
If the value of the resistor \[R_2\] were doubled, how would the value of 
the resistor \[R_3\] have to change in order to keep the current 
through \[R_4\] equal to zero?

* \[R_3\] would need to be decreased
  * \[I_2 = \frac{ V_2}{ R_2}\] would be decreased by half if 
    \[R_2\] were doubled, hence \[R_3\] needs to be decreased.


## Circuit 2 with Resistors and a Battery
A circuit is constructed with five resistors and a battery 
as shown. The values for the resistors are: \[R_1 = R_5 = 63.0 \Omega\], 
\[R_2 = 81.0 \Omega\], \[R_3 = 64.0 \Omega\], and \[R_4 = 130.0 \Omega\]. 
The battery voltage is \[V = 12.0 V\].

[[circuit_2.png]]

Let
* \[V_0 = V = 12.0 V\]
* \[R_1 = R_5 = 63.0 \Omega\]
* \[R_2 = 81.0 \Omega\]
* \[R_3 = 64.0 \Omega\]
* \[R_4 = 130.0 \Omega\]

### 1)
What is \[R_{ab}\], the equivalent resistance between points \[a\] and \[b\]?

* \[R_{ab} = \left(\frac{ 1}{ R_2 + R_3} + \frac{ 1}{ R_4}\right)^{-1}\]
  * Correct

* \[R_2 + R_3\]
  * It looks like you have calculated the equivalent resistance of \[R_2\] 
    and \[R_3\] in series. These resistors are not the only resistors connected
    between \[a\] and \[b\]. Try redrawing the circuit after finding \[R_{23}\] to 
    see what else you must take into account.


### 2)
What is \[R_{ac}\], the equivalent resistance between points \[a\] and \[c\]?

* \[R_{ac} = R_1 + R_{ab} = R_1 + \left(\frac{ 1}{ R_2 + R_3} + \frac{ 1}{ R_4}\right)^{-1}\]

### 3)
What is \[I_5\], the current that flows through resistor \[R_5\]?

* \[I_5 = I_{equiv} - I_{ac}\]
  * \[I_{equiv} = \frac{ V_0}{ R_{equiv}}\]
      * R_{equiv} = R_1 + \left(\frac{ 1}{ R_2 + R_3} + \frac{ 1}{ R_4}\right)^{-1} + R_5}
  * \[I_{ac} = I_1 - I_{bc} \]
  * \[V_b = V_0 - V_1\]
      * \[V_1 = R_1 I_1 = R_1 \frac{ V_0}{ R_equiv}\]
  * \[V_a = V_0 - V_1 - V_4\]
      * \[V_4 = R_4 I_4 = R_4 \frac{ V_b}{ R_4 + R_5 }\]


### 5)
What is \[I_1\], the current that flows through the resistor \[R_1\]?

* \[I_1 = \frac{ V_0}{ R_equiv}\]
