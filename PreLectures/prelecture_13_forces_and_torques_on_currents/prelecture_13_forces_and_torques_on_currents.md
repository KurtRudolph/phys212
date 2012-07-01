# Forces and Torques on Currents

## Overview
* Continue study of magnetism by studying the forces and torques
  exerted on currents carrying wires and magnetic fields.
  * First, calculate the forces on strait and curved wires in
    constant magnetic fields
  * Next, calculate the torque on a closed loop of current in a magnetic
    field.
  * Next, introduce the concept of the dipole moment.
  * Last, we use this dipole moment to define the _potential_ energy that is associated
    with a current loop located in a region of space that contains a magnetic field.

## Forces on a Straight Current Segment
* Last time, we learned charges moving in a uniform magnetic field experience a force that
  is proportional to the charge, magnetic field, and component of the velocity perpendicular
  to the magnetic field.  The direction is perpendicular to both the magnetic field and
  the velocity.
* Now, we discuss what happens when a current carrying wire is placed in a region of space
  that contains a magnetic field.
  * [[cur_wire_mag_field.png]]
  * Current is composed of charges in motion we expect that there will be some sort of
    force exerted on the wire.
  * [[cur_wire_mag_field_1.png]]
  * Using the right hand rule we determine the force to be in the upward direction
  * Now calculate the magnitude of this force.
  * \[\vec F = I \vec L \times \vec B\]
      * \[\vec F = \sum\limits_{i}{ \vec F_i} 
        = q \sum\limits_{i}{ \vec v_i \times \vec B\]
      * \[= q (N \vec v_{avg}) \times \vec B \]
          * \[N = n A L\] where \[n\] is the number of charges carriers per volume in the wire
            and \[A L\] is the volume of the wire.
      * \[= q n A L \vec v_{avg} \times \vec B\]
          * \[I = n A q v_{avg}\]
      * The net force is vector sum of the force acting on 
        each of the individual charges carried through the wire.
      * Since the charges are constrained within the wire it is also the
        net force on the wire.

## Question 1
What units result when a velocity \[v\] is multiplied by an area \[A\]?

* Volume per second
  * The units of velocity are \[\frac{ m}{ s}\] and the units of area 
    are \[m^2\], and when we multiply these together we get \[\frac{ m^3}{ s}\]
    which is volume per second.
  * A simple and useful way to picture this is to think of water flowing in a 
    garden hose. If the speed of the water is known, 
    \[v = 10 \frac{ m}{ s} = 1,000 \frac{ cm}{ s}\] for example, 
    and the cross-sectional area of the hose is also known,
    \[A = 10 cm^2\] for example, then the volume of water that 
    travels past any point of the hose is every second is 
    \[v A = 10,000 \frac{ cm^3}{ s} = 10 \frac{ liters}{ s}\]. 
    In other words, if we know the velocity of the water and the 
    area of the hose we can easily figure out the volume of water 
    transported by the hose per unit time. If we multiply this by 
    the density of water, i.e.
    \[10 \frac{ liters}{ s} \frac{ kg}{ liter} = 10 \frac{ kg}{ s}\],
    then we immediately discover how much mass is moving past a point 
    in the hose the hose per unit time.
  * This has an exact analogy with current in a wire. Think of the wire 
    as the hose and the current flowing in the wire as the water. The 
    average velocity of the charges \[v_{avg}\] times the area of the 
    wire \[A\] tells us the volume of the charge carriers that moves 
    through the wire per unit time. If we multiply this by the number 
    density of the charge carriers n we find the number of charge 
    carriers per unit time flowing in the wire, and if we multiply 
    this by the charge carried by each one \[q\] we find the charge 
    per unit time flowing in the wire.
  * In other words, the current in the wire 
    \[I\] is equal to the product \[q n A v_{avg}\].

## Force on a curved current segment
* Consider the wire to be made up of sufficiently small wire segments
  \[s\] and look at the vector sum of the force on these segments to get
  the net force on the wire.
  * \[\vec F_{wire} = \sum \vec F_{i} 
    = \sum\limits_{i}{ I d \vec s_i \times \vec B}
    = \int{ I d \vec s \times \vec B}\]
  * \[= \int I d \vec s_{\|} \times \vec B + \int I d \vec s_{\perp} \times \vec B\]
  * \[= \int I d \vec s_{\perp} \times \vec B\]
      * since \[\int I d \vec s_{\|} \times \vec B = 0\]
  * \[= I B \int d s_{\perp}\]
      * since \[I\] and \[B\] are constant
  * \[= I B (L_{\perp}) = I \vec L \times \vec B\]
  * [[curved_wire.png]]
  * The force on the wire does not depend on the exact shape of the wire but rather only the distance    between the perpendicular components of the wire.
