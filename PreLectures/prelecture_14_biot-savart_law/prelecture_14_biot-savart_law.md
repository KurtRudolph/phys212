# Biot-Savart Law

## Overview
* Until now, we have taken magnetic fields to be a given
* Now, we will examine how magnetic fields are created
  * Magnetic fields are produced by electric currents
  * We can calculate magnetic fields produced by current 
    distrobutions using the _Biot-Savart Law_
* Start, by examining the magnetic field produced by an 
  infinite current carrying wire.
* Next, we use the result we found to examine the forces exerted
  by parallel current carrying wires
  * [[current_carrying_parallel_wires.png]]
* Finally, we calculate the magnetic field along the axis of a 
  circular current carrying loop.
  * [[current_carrying_loop.png]]

## Biot-Savart Law
* \[d \vec B = \frac{ \mu_0 I}{ 4 \pi} \frac{ d \vec s \times \hat r}{ r^2}\]
  * [[biot-savart_law.png]]
  * The magnetic field \[d \vec B\] that is produced by current \[I\] in a 
    segment of length \[d \vec s\] at a point that is a distance \[\vec r\]
    from the segment is given by the above expression.
  * \[\mu_0 = 4 \pi \times 10^{-7} \frac{ T \cdot m}{ A}\]
      * \[\frac{ T \cdot m}{ A} \Rightarrow\] Tesla metters per aplitude.
  * Direction of \[d \vec S\] is in that of the current, the direction of the positive charge
  * \[\vec r\] is a vector from the segment to the point at which we want to determine the
    magnetic field.
  * Direction of the magnetic field is determined by \[d \vec s \times \hat r\]
      * Right hand rule
          * Fingers point in direction of \[d \vec s\]
          * Curl fingers toward \[\vec r\]
          * Thumb gives direction of \[d \vec B\]
      * For the case in the image above the direction of the magnetic field is into the screen. 

## B from Infinite Straight Wire
* \[B = \frac{ \mu_0 I}{ 2 \pi R}\]
  * \[\vec B = \int d \vec B = \frac{ \mu_0 I}{ 4 \pi} \int \frac{ d \vec s \times \hat r}{ r^2}\]
      * Biot-Savart Law
  * [[infinite_strait_wire.png]]
      * \[r = \frac{ R}{ \cos \alpha}\]
      * \[x = R \tan \alpha\]
      * \[ds = dx = \frac{ R}{ \cos^2 \alpha} d \alpha\]
  * For all segment the magnetic fiel is out of the screen
  * \[\vec B = \frac{ \mu_0 I}{ 4 \pi} \int \frac{ d \vec s \times \hat r}{ r^2}\]
  * \[= \frac{ \mu_0 I}{ 4 \pi} \int \frac{ \sin \theta ds}{ r^2} \hat z\]
  * \[= \frac{ \mu_0 I}{ 4 \pi} \int\limits_{-\frac{ \pi}{ 2}}^{\frac{ \pi}{ 2}}{ \frac{ \cos \alpha}{ r^2} \frac{ R}{ \cos^2 \alpha} d \alpha \hat z}\]
  * \[= \frac{ \mu_0 I}{ 4 \pi} \int\limits_{-\frac{ \pi}{ 2}}^{\frac{ \pi}{ 2}}{ \frac{ \cos \alpha}{ \left(\frac{ R}{ \cos \alpha}\right)^2} \frac{ R}{ \cos^2 \alpha} d \alpha \hat z}\]
  * \[= \frac{ \mu_0 I}{ 4 \pi} \int\limits_{-\frac{ \pi}{ 2}}^{\frac{ \pi}{ 2}}{ \cos \alpha d \alpha \hat z}\]
  * \[=  \frac{ \mu_0 I}{ 4 \pi R} 2 = \frac{ \mu_0 I}{ 2 \pi R}\]

## Infinite Straight Wire: A Discussion
* We now want to discuss some of the features of this result for the magnetic field
  of an infinite linear current.
  * \[B = \frac{ \mu_0 I}{ 2 \pi R}\]
  * The magnitude of the field is proportional to \[\frac{ I}{ R}\]
      * [[discusion_prop_mag_i_r.png]]
      * Similar to that of the electric field of an infinite line of charge
      * Charge Element  \[d \vec E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ d q}{ r^2} \hat r\]
      * Current Element \[d \vec B = \frac{ \mu_0 I}{ 4 \pi} \frac{ d \vec s \times \hat r}{ r^2}\]