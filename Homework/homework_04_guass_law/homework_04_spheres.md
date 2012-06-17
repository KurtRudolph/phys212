# Spheres

[[spheres.png]]

An insulator in the shape of a spherical shell is shown in cross-section above. 
The insulator is defined by an inner radius \[a = 4.0 cm\] and an outer radius 
\[b = 6.0 cm\] and carries a total charge of \[Q = + 9.0 \mu C\]. (You may 
assume that the charge is distributed uniformly throughout the volume of 
the insulator). What is \[E_y\], the \[y\]-component of the electric field at point 
\[P\] which is located at \[(x,y) = (0 m, -5.0 cm)\] as shown in the diagram?

* Let
  * \[a = 4.0 cm = 0.04 m\]
  * \[b = 6.0 cm = 0.06 m\]
  * \[Q = 9.0 \mu C\]
  * \[(x, y) = (0 m, -5.0 cm) = (0 m, -0.05 m) = \]
* Given
  * For sphical insulators with a point charge \[Q\] at the center:
  * \[V_{sphere} =  \frac{ 4}{ 3} \pi r^3\]
  * \[A_{sphere} = 4 \pi r^2\]
  * Guass' Law of Symmetry
      * \[ E \oint\limits_{surface}{ dA} = \frac{ q_enclosed}{ \varepsilon_0}\]
* Wrong answers  
  * \[E = \frac{ Q}{ 4 \pi \varepsilon_0 r^2} = 3.23705E7\]
      * It looks like you are treating this distribution as a point charge of 
        \[Q = 9.0 \mu C\] located at the origin. The charge distribution is a 
        little more complicated that that.
* Help
  * What is \[q_{enclosed}\], the charge enclosed by the Gausian sphere?
      * \[q_{enclosed} = \frac{ Q}{ 4 \pi 100 \left((b)^2 - (a)^2\right)} = 3.23705E7\]
          * I have no idea why it is dividing by \[100\]!
* \[E = \frac{ q_{enclosed}}{ A \varepsilon_0} = -1.28798E7\]