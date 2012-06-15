# Electric Potential Energy 

## Overview
* Coulomb Force
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r}\]
  * The work done by the Coulomb Force is independent from the path between those two points
  * A conservative force.

## Work Done by Coulomb Force
* \[W_{AB} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left( \frac{ 1}{ r_A} - \frac{ 1}{ r_B}\right)\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2} \hat r\]
  * \[W_{A \rightarrow B} = \int\limits_{r_A}^{r_B}{ \vec F_E \cdot d \vec r}\]
    * \[\vec F_E\] and \[d \vec r\] are always in the same direction.
  * \[W_{A \rightarrow B} = \int\limits_{r_A}^{r_B}{ F_E \cdot d r}\]
  * \[W_{A \rightarrow B} = \int\limits_{r_A}^{r_B}{ \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2} d r}\]
  * \[W_{A \rightarrow B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \int\limits_{r_A}^{r_B}{ \frac{ 1}{ r^2} d r}\]
  * \[W_{A \rightarrow B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left[-\frac{ 1}{ r} \right]\limits_{r_A}^{r_B}\]
  * \[W_{A \rightarrow B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_A} - \frac{ 1}{ r_B}\right)\]

## Question 1
Masses \[M_1\] and \[M_2\] are initially separated by a distance \[R_a\]. 
Mass \[M_2\] is now moved further away from mass \[M_1\] such that their 
final separation is \[R_b\].

Which of the following statements best describes the work \[W_{ab}\] done 
by the force of gravity on \[M_2\] as it moves from \[R_a\] to \[R_b\]?

[[images/prelecture_05_q1.png]]

* \[W_{ab} < 0\]
  * Since the gravitational force on \[M_2\] and the displacement of 
    \[M_2\] are in the opposite direction, the work done by the force 
    of gravity as \[M_2\] moves is negative.

[[images/prelecture_05_q1a.png]]


## Coulomb Force is a Conservative Force
* \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r}\]
* \[W_{AB} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left( \frac{ 1}{ r_A} - \frac{ 1}{ r_B}\right)\]

## Electric Potential Energy
* \[U_r \equiv \Delta U_{\infty r} = \frac{ Q q}{ 4 \pi \varepsilon r}\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r}\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r} \rightarrow U\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r} \rightarrow \Delta U = -W\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r} \rightarrow \Delta U_{A B} = -\frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_A} + \frac{ 1}{ r_B}\right)\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r} \rightarrow \Delta U_{A B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(-\frac{ 1}{ r_A} + \frac{ 1}{ r_B}\right)\]
  * \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r} \rightarrow \Delta U_{A B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_A}\right)\]
  * Change in Potential Energy: 
      * \[\Delta U_{A B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_A}\right)\] 
      * \[\Delta U_{r_0 B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_0}\right)\] 
      * \[\Delta U_{\infty B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ \infty}\right)\] 
          * Since were dealing with point charges aparently it's natural to let \[r_0\] to be infinity (i.e. _magic_).
      * \[\Delta U_{\infty B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B}\right)\] 
      * \[\Delta U_{\infty r} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r}\right)\] 
      * \[U_r \equiv \Delta U_{\infty r} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r}\right)\] 
      * \[U_r \equiv \Delta U_{\infty r} = \frac{ Q q}{ 4 \pi \varepsilon r}\]

## Question 2
n Case A two charges which are equal in magnitude but opposite in charge are separated by a distance \[d\]. In Case B the same charges are separated by a distance \[2d\].

Which configuration has the highest potential energy \[U\]?

[[images/prelecture_05_q2.png]]

* Case B has the highest potential energy
  * The plot of \[U(r)\] shown below helps illustrate why this answer is correct. As the 
    separation of the charges is increased we move to the right along the blue plot shown. 
    Since the plot is going upward as we move to the right, U is increasing with separation.

[[images/prelecture_05_q2a.png]]


## Example: Calculated Speed
* \[v = \sqrt{ \frac{ q_1 q_2}{ 2 \pi \varepsilon_0 m_2} \left(\frac{ 1}{ d} - \frac{ 1}{ x}\right)}\]