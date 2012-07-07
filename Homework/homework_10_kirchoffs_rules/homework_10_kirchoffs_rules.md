# Homework: Kirchoff's Rules

## Current Div
The circuit above contains 5 resistors \[R_1, R_2, R_A, R_B, R_C\] 
with equal resistance \[R\]. Write an equation for the current \[i_2\] 
in terms of the current \[i_1\]. ( when entering your answer, use 
i1 for \[i_1\], e.g., the answer 0.5*i1 has the correct syntax)

* \[I_2 = \frac{ 1}{ 3} I_1\]
  * see octave code

## Multiloop

Resistors \[R_1, R_2, R_3, R_4\] are arranged in a circuit 
as shown in the figure above. The direction of positive currents 
\[I_1, I_2, I_3, I_4\] through the resistors are shown. 
(i.e., negative current values correspond to currents in the opposite 
direction to that shown above). The values for the resistors and the 
batteries in the circuit are: \[R_1 = 100.0 \Omega, R_2 = 200.0 \Omega, 
R_3 = 30.0 \Omega, R_4 = 400.0 \Omega, V_1 = 4.0 V, V_2 = 12.0 V\]. 
What is the value of \[I_2\], the current through \[R_2\]? 
(remember \[I_2\] is a signed number) 

\[I_2 =\]

### Help

#### Conceptual Analysis
The first step in solving physics problems is a CONCEPTUAL ANALYSIS. 
The first thing to consider is whether it is reasonable that there 
should be a current through \[R_2\]. Select all of the following statements 
that MUST be true in order to produce a current through \[R_2\] in the above circuit.

* There is at least one closed loop (completed circuit) containing R2.
  * Check
* There is a battery in at least one closed loop containing R2.
  * Check
* There is a battery in every closed loop containing R2.
  * Wrong

Currents exist only in closed circuits and there must be some source of 
potential difference in that closed circuit. Here the battery is responsible 
for the potential difference. It is not necessary to provide a source in every 
closed circuit that contains \[R_2\], however. Consider for example a circuit 
consisting of a battery connected to the parallel combination of two resistors. 
There will be currents through both resistors but there will be one loop which 
has no battery (the loop containing just the two resistors). 

Note that, in general, the source of potential difference would not have to be 
a battery. For example a circuit consisting of a resistor and an initially charged 
capacitor (which creates the potential difference) will have a current. This current 
will not be sustained, however, as the capacitor discharges and thereby the 
potential difference decreases in time. More on this possibility next week.


Now we know why it is reasonable to expect a current through R2 in this circuit. 
In order to calculate the value of this current, we will need to apply some laws 
of physics. Which one of the following laws of physics would you expect to be the 
most helpful to us in determining \[I_2\]?

* Kirchoff's Laws

 Kirchhoff's Laws are designed exactly to make this kind of calculation. 
Kirchhoff's Laws should be the first thing you think of when confronted with 
a circuit problem. They always work. Of course, sometimes the problem is special 
enough that the circuit can be solved more naturally 'by inspection'.

Now we know that we will attempt to solve this problem using Kirchhoff's Laws. 
Before we leave this conceptual analysis section, however, let's be clear as 
to the source of Kirchhoff's Laws. They are not something 'new'. These Laws 
are really the application of more general laws to particular physical situations 
that involve electric circuits. 

Kirchoff's Junction Law states that the sum of the currents into a junction 
is equal to the sum of the currents leaving the junction. This statement is a 
direct application to electric circuits of what more general physical principle?

* Conservation of Charge

Conservation of Charge states that there is no physical process that can create 
or destroy charge. When you 'create' a positive charge on a glass rod by rubbing 
it with a silk cloth, you also 'create' an equal amount of negative charge on the 
silk cloth. 

If we apply this law to electric circuits we can say that charge cannot be created 
or destroyed at any point in the circuit. If we focus on a junction point, this law 
becomes Kirchhoff's Junction Law: the total current (or the charge in a specified 
amount of time) entering a junction is equal to the total current leaving the junction.

Now we know Kirchhoff's Junction Law is a direct application of the more general 
Principle of the Conservation of Charge. Kirchhoff's Loop Law states that the sum 
of the voltage drops around any closed loop is zero. This statement is a direct 
application to electric circuits of which of the following familiar concepts?

* The potential difference between two points is path independent

The power of the concept of Potential is that it is a 'property of the space'. 
A given distribution of charge produces an electric field that is defined at 
every point in space. The potential difference between any two points in space is 
determined by integrating that electric field between the two points. This 
integral is 'independent of the path' which is chosen between those two points. 

We can directly apply this principle to electric circuits by first noting 
that the potential difference between a point and itself must be zero. Since 
the potential difference is independent of path, we can follow any closed loop 
in the circuit and simply add up the potential differences (voltage drops) 
across the circuit elements (resistors and batteries in this case) and we 
must get zero, the potential difference between a point and itself.

#### Strategic Analysis
The next step in solving physics problems is a STRATEGIC ANALYSIS.
We now need to develop a strategy for determining \[I_2\]. What is the 
minimum number of equations we need to write down to be able to apply 
Kirchhoff's Laws to this circuit to determine \[I_2\]?

* Two Loop Equations and One Junction Equation

At first glance it looks like we will need to apply Kirchhoff's Laws to 
three loops. However, on closer inspection, we see that the third loop 
(\[V_2\] and \[R_4\]) is not really coupled to the other loops. \[R_3\] 
couples the first two loops. Therefore we need to solve for three variables, 
\[I_1\], \[I_2\], and \[I_3\]. This procedure requires three equations. 
There is only one junction equation needed to relate \[I_1\], \[I_2\], 
and \[I_3\]. Consequently, we must find the other two equations from 
application of Kirchoff's Loop Law.

We have now completed the STRATEGIC ANALYSIS. We know we need to write 
down two loop equations and one junction equation in order to solve 
for \[I_1\], \[I_2\], and \[I_3\]. If you see how to do this, go ahead 
and choose your loops, write down the equations and solve them. If you 
would like some help with this procedure, click below to continue.

#### Quantitative Analysis
The final step in solving a physics problem is the QUANTITATIVE ANALYSIS
Now we know we need to write three independent equations for \[I1, I2, I3\]. 
Let's begin with the one needed junction equation. 

Which of the following equations can be obtained by an application of 
Kirchhoff's Junction Law to this circuit?

* \[I_1 = I_2 + I_3\]

If we apply Kirchoff's Junction Law to the point marked A below, we see 
that the total current coming into point A is \[I_1\] and the total 
current leaving point A is \[I_2 + I_3\]. Note that it may turn out 
that one or more of these currents will be found to be negative. 
For example, if \[I_3\] turns out to be negative, then it is really 
a current that is coming into point A rather than leaving it. That's 
just fine, however, a negative outgoing current is the same thing as 
a positive incoming current. It all comes out in the wash.

[[multiloop_quantitative.png]]


## Circuit with Two Batteries and Six Resistors
A circuit is constructed with six resistors and two batteries as shown. 
The battery voltages are \[V_1 = 18.0 V\] and \[V_2 = 12.0 V\]. The 
positive terminals are indicated with a \[+\] sign, The values for the 
resistors are: 
\[R1 = R5 = 52.0 \Omega, R2 = R6 = 93.0 \Omega, R3 = 41.0 \Omega, R4 = 107.0 \Omega\]. 
The positive directions for the currents [\I_1, I_2, I3\] are indicated by the 
directions of the arrows.

[[circuit_two_bat_six_resis.png]]


## Non-Ideal Battery
A circuit is constructed with five resistors and one real battery as shown above 
right. We model. The real battery as an ideal emf \[V = 12.0 V\] in series with 
an internal resistance \[r\] as shown above left. The values for the resistors 
are: \[R_1 = R_3 = 43.0 \Omega, R_4 = R_5 = 84.0 \Omega, R_2 = 150.0 \Omega\]. 
The measured voltage across the terminals of the batery is \[V_{battery} = 11.8 V\].

[[non-ideal_battery.png]]

### 1

