# Gauss' Law

## Overview

* \[ \oint\limits_{surface}{ \vec E \cdot d \vec A} = \frac{ q_{enclosed}}{ \epsilon_0} \]
* First discuss solid insulator followed by 
* Solid Conductor
* Cylindrical Conductor
* Infinite Sheet of Charge

## Gauss' Law and Symmetry

* Casses with Symmetry \[ E\] may be pulled out of Gauss' Law such that
  * \[E \oint\limits_{surface}{ d A} = \frac{ q_{enclosed}}{ \epsilon_0}\]

## Question 1

Consider a sphere, an infinitely long cylinder, and a plane of infinite length 
and width (a, b and c below). Imagine that you can hover above each one in your 
own personal helicopter. In which case do you have the most freedom to move about 
without your view of the object changing? In other words, for each case consider 
if there are directions that you can move in without the objects distance or 
orientation, relative to you, changing.

[[images/prelecture_04_gauss_law_q1.png]]

* The infinite plane offers the most freedom to move without your view changing.
  * You can move in two dimensions - any direction parallel to the plane - as you 
    fly above it, and it will still look exactly the same from your perspective. 
    By the same kind of reasoning you will see that you can move in just one 
    dimension above the cylinder - parallel to its length - if you want it to 
    look the same, and you can not move at all above the sphere without your 
    view changing.

[[images/prelecture_04_gauss_law_q1a.png]]


## Solid spherical Insulator: Part I
* Insulator \Rightarrow charges cannot move
* Let 
  * \[Q \] be the charge
  * \[a \] be the radius
* \[ E = \frac{ Q}{ 4 \pi \epsilon_0 r^2}\]

## Question 2

A solid sphere of radius \[R\] has a total charge \[ Q\] distributed evenly throughout 
its volume. What fraction of the total charge is located inside a radius \[ \frac{ R}{ 2} \]?

[[images/prelecture_04_gauss_law_q2.png]]

* \[ \frac{ 1}{ 8} \]
* Since the charge is uniformly distributed throughout the volume of the sphere, the fraction 
  of the charge that resides inside a given radius is simply equal to the fraction of the spheres 
  volume inside that radius. Since the volume of a sphere is \[ 4 \pi \frac{ R^3}{ 3} \], reducing the 
  radius by \[\frac{ 1}{ 2}\] will reduce the volume by \[ \left(\frac{ 1}{ 2}\right)^3 = \frac{ 1}{ 8}\].

## Solid Spherical Insulator: Part II
* Insulator \Rightarrow charges cannot move
* Let 
  * \[Q \] be the charge
  * \[a \] be the radius
  * \[r \] distance of the test point
* Charge Density
  * \[ \rho = \frac{ Q}{ \frac{ 4}{ 3} \pi a^3} \]
* \[r > a\]
  * \[ E = \frac{ Q}{ 4 \pi \epsilon_0 r^2}\]
* \[r < a \]
  * \[ E = \frac{ \rho}{ 3 \epsilon_0} r \]

## Question 3

Consider a sphere of radius \[ R\], surface area \[ A\] and volume \[ V\]. Suppose you double the 
radius to \[2R\]. How does the new surface area \[A_{new}\] and the new volume \[V_{new}\] 
compare to the old values?

[[images/prelecture_04_gauss_law_q3.png]]

* \[A_{new} = 4A, V_{new} = 8V\]
  * The area of a sphere is given by \[ A = 4 \pi R^2\] and the volume of a sphere is given by 
\[ V = \frac{ 4 \pi R^3}{ 3}\]. Doubling \[ R\] in each case will cause the volume to increase 
by a factor of \[ 2^3 = 8\] and the area to increase by a factor of \[ 2^2 = 4\].


## Conductor Charges are on Surface
* Solid Conductor
  * Charge is on the surface
  * Charge free to move
  * Inside the sphere
      * \[ E = 0\]

## Induced Charges on Conductors
[[images/prelecture_04_gauss_law_induced_charges_on_conductors.png]]

* Let
  * \[ Q_{inner} = -q_0 \]
* Then
  * \[ \sigma_i = \frac{ -q_0}{ 4 \pi R_i^2 \]
      * Induced Inner Charge Density

* Let
  * \[ Q_{Outer} = Q + q_0 \]
* Then
  * \[ \sigma_0 = \frac{ Q + q_0}{ 4 \pi R_0^2}\]
      * Outer Charge Density

## Solid Cylindrical Conductor
* \[ E = \frac{ \lambda}{ 2 \pi \epsilon_0 r}
  * \[ \lambda \Rightarrow\] linear charge density

## Infinite Sheet of Charge
* \[ E = \frac{ \rho}{ 2 \epsilon_0 } \]

## Question 4
You are told to use Gauss' law to calculate the electric field near an 
infinite sheet. The catch is that you have to choose a Gaussian surface 
different from the one used in the previous example. Which of the following 
Gaussian surfaces is best suited for this purpose?

[[images/prelecture_04_gauss_law_q4.png]]

* a sphere centered on the plane
* a cylinder with its axis parallel to the plane
* a box with two sides parallel to the plane
  * This one!
  * The sides of the box are either perpendicular or parallel to the field, 
    so this Gaussian surface is just as good as the perpendicular cylinder 
    used in the above example.


[[images/prelecture_04_gauss_law_q4a.png]]

## Summary

* \[ \oint\limits_{surface}{ \vec E \cdot d \vec A} = \frac{ q_{enclosed}}{ \epsilon_0} \]

* Let
  * \[ Q_{inner} = -q_0 \]
* Then
  * \[ \sigma_i = \frac{ -q_0}{ 4 \pi R_i^2 \]
      * Induced Inner Charge Density

* Let
  * \[ Q_{Outer} = Q + q_0 \]
* Then
  * \[ \sigma_0 = \frac{ Q + q_0}{ 4 \pi R_0^2}\]
      * Outer Charge Density

