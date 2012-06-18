# Electric Potential

## Overview
* Electric Potential Energy
  * \[U \propto q\]
  * Electric potential energy is proportional to it's charge.
  * Hence we are able to define a new quantity Electric Potential
* Electric Potential
  * \[V \equiv \frac{ U}{ q}\]
  * Similar to Electric Field
      * \[\vec E \equiv \frac{ \vec F_{Coulomb}}{ q}\]

## Electric Potential V
[[images/prelecture_06_electric_potential_v.png]]

* Electric Potential Energy
  * \[U \propto q\]
* Electric Potential Difference
  * \[\Delta V \equiv \frac{ \Delta U}{ q}\]
      * The change in electric potential energy per unit charge
      * \[W_{A \rightarrow B} = \int\limits_{A}^{B}{ \vec F \cdot d \vec l}\]
          * Electric Potential Energy
      * \[W_{A \rightarrow B} = \int\limits_{A}^{B}{ q \vec E \cdot d \vec l}\]
          * We can express the Coloumb force at at any point along the path from 
            \[A\] to \[B\] as the product of the charge and the electric field.
      * \[\Delta U_{A \rightarrow B} = -\int\limits_{A}^{B}{ q \vec E \cdot d \vec l}\]
          * \[\Delta U_{A \rightarrow B} = -[W_{A \rightarrow B}\]
      * \[\Delta U_{A \rightarrow B} = -q \int\limits_{A}^{B}{ \vec E \cdot d \vec l}\]
          * Note that the change in potential energy is proportional to the charge \[q\]
      * Therefore \[\Delta V_{A \rightarrow B} \equiv \frac{ \Delta U_{A \rightarrow B}}{ q} = -\int\limits_{A}^{B}{ \vec E \cdot d \vec l}\]

[[images/prelecture_06_electric_potential_v_example.png]]

* Electric potential difference
  * \[\Delta V_{A \rightarrow B} \equiv \frac{ \Delta U_{A \rightarrow B}}{ q} = -\int\limits_{A}^{B}{ \vec E \cdot d \vec l}\]
* Electric Field
  * \[\vec E = k \frac{ Q}{ r^2} \hat r\]
* \[\Delta V_{A \rightarrow B} = -\int\limits_{A}^{B}{ \vec E \cdot d \vec l}\]
* \[\Delta V_{A \rightarrow B} = -\int\limits_{A}^{B}{ k \frac{ Q}{ r^2} \hat r \cdot d \vec r}\]
* \[\Delta V_{A \rightarrow B} = k Q \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_A}\right)\]
    * The electric potential difference is proportional to inverse distances from the point charge.
* \[V( r) = \fra{ k Q}{ r}\]
  * When we let \[r_0 = \infty\]
  * \[V( r) \equiv \Delta V_{r_0 \rightarrow r} = k Q \left(\frac{ 1}{ r} - \frac{ 1}{ r_0}\right)\]
      * It is common to introduce a quantity \[V( r)\] which is defined for each single point in space

* SI Units are \[V = \frac{ J}{ C}\] or volts equals joules per coulomb


## E from V
* We just defined Electric Potential \[V( r) = -\int\limits_{_r_0}^{r}{ \vec E \cdot d \vec r}\]
* We are able to take the derivative of the electric potential to determine the electic fieled
  * \[\vec E( r) = -\frac{ dv}{ dr} \hat r\]

### Example
[[images/prelecture_06_e_from_v_example.png]]

* \[V( r) = k \frac{ Q}{ r}\]
* \[E = -\frac{ dV}{ dr}\]
* \[E = -\frac{ d}{ dr} \left( k \frac{ Q}{ r}\right)\]
* \[E = -\left(-k \frac{ Q}{ r^}\right)\]
* \[E = k \frac{ Q}{ r^}\]

### In Multiple Dimensions...
* \[\vec \nabla V = \frac{ \partial V}{ \partial x} \hat i + \frac{ \patial V}{ \partial y} \hat j \frac{ \partial V}{ \partial z} \hat k\]
    * \[\vec \nabla V\] is the gradient of potential