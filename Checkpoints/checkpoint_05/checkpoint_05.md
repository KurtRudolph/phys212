# CheckPoint: Electric Potential Energy

## Electric Potential Energy of Point Charge
A charge of \[+Q\] is fixed in space. A second charge of \[+q\] was 
first placed at a distance \[r_1\] away from \[Q\]. Then it was moved 
along a straight line to a new position at a distance \[R\] away from 
its starting position. The final location of \[+q\] is at a distance \[r_2\] from \[+Q\].

[[images/electric_potential_energy_of_point_charge.png]]

What is the change in the potential energy of charge \[+q\] during this process?

* \[k \frac{ Q q}{ r_2 - r_1}\]
  * \[\Delta U_{r_1 \rightarrow r_2} = U_{r_2} - U_{r_1} = k \frac{ Q q}{ r_2} - \frac{ Q q}{ r_1} = k Q q \left( \frac{ 1}{ r_2} - \frac{ 1}{ r_1}\right)\]

## Lecture Thoughts

Why are the variables continually changing? Why does physics need to be such a giant back story?

Specifically:
* PreLecture: Done by Coulomb Force
  * You introduce Coulombs law as \[\vec F_E = \frac{ 1}{ 4 \pi \varepsilon_0} \frac{ Q q}{ r^2}\hat{ r}\], siting the charges in terms of  \[Q\] and \[q\].
  * You then introduce the conservation formula \[W_{AB} = \frac{ q_1 q_2}{ 4 \pi \varepsilon_0} \left( \frac{ 1}{ r_A} - \frac{ 1}{ r_B}\right)\]
  * Why did you change these, this is just confusing and unnecessary.
* PreLecture: Question 1
  * You state the question in terms of \[M_1\], \[M_2\], \[R_a\], \[R_b\].  
  * The conservation formula \[W_{AB} = \frac{ q_1 q_2}{ 4 \pi \varepsilon_0} \left( \frac{ 1}{ r_A} - \frac{ 1}{ r_B}\right)\] is defined with points \[A\] and \[B\] with distances \[r_A\] and \[r_B\].
  * Why did you change these, this is just confusing and unnecessary.
* PreLecture: Electric Potential Energy
  * While explaining where the equation for Electric Potential Energy came from you have the following irregularities:
      * Jump from \[U_{AB} \Rightarrow r_A, r_B\] to \[U_{r_0 B} \Rightarrow r_0 r_B\]
          * \[\Delta U_{A B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_A}\right)\] 
          * \[\Delta U_{r_0 B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B} - \frac{ 1}{ r_0}\right)\] 
      * Jump from \[U_{\infty B} \Rightarrow infty r_B\] to \[U_{\infity r} \Rightarrow \infty r\] 
          * \[\Delta U_{\infty B} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r_B}\right)\] 
          * \[\Delta U_{\infty r} = \frac{ Q q}{ 4 \pi \varepsilon_0} \left(\frac{ 1}{ r}\right)\] 
  * This expression are **not** regular!
* PreLecture: Question 2
  * distance in now in terms of \[d\]
  * charges switch from \[q_1, q_2\] to just \[-q\] and \[+q\]
  * Where is the consistency, why do I constantly have to unnecessarily infer meaning out these problems.  This does not help people learn it just make them approach the problems as if physics is magic.* PreLecture Example: Calculated Speed
  * You define velocity as follows: \[v = \sqrt{ \frac{ q_1 q_2}{ 2 \pi \varepsilon_0 m_2} \left(\frac{ 1}{ d} - \frac{ 1}{ x}\right)}\]
      * In this definition, \[x\] and \[d\] are completly arbitrary!
  * Why not define it as \[v(r) = \sqrt{ \frac{ Q q}{ 2 \pi \varepsilon_0 m_2} \left(\frac{ 1}{ r_0} - \frac{ 1}{ r}\right)}\]
      * Stick to a convention and use \[r\]
      * The original formula is a function of \[x\], lets make it a functions of our substituted \[x\], \[v(r)\]
      * \[d\] isn't some magical value, it is the original distance we are calculating from, why not make it \[r_0\], no long winded explanation need to figure out what that is anymore.
* PreLecture: Question 3
  * Why do the point charges have labels which are their magnitudes, where is the consistency amongst these examples?
* PreLecture: Summary
  * Why is \[N\] the number of charges? Capital letters generally represent a set and \[N\] often represents the set of natural numbers, this is just confusing!
      * Why not say: Let \[P\] be a system \[n\] charged particles where \[ n,\in N\].  Let \[ i,j \in N, and 0 \le i \le j \le (n - 1)\].  Then \[U_P = k \sum\limits_{i = 0}^{n - 2}{ \sum\limits_{j = i + 1}^{n - 1}{ \frac{ q_i q_j}{ r_{ij}}}}\].  Now students can pull logical meaning out of the formula rather than just accepting it as magic.

The laws of physics are able to be defined as a [regular language](http://en.wikipedia.org/wiki/Regular_language).  The manor in which formulas are presented often requires unnecessary interpretation of what the variables actually mean.
If the material consistency state logical meaning amongst the various formulas, these long winded explanations about what the formulas are and how they are derived would be unnecessary.  
The material of this course is trivial, the way it is presented and manor in which the questions are formulated makes learning the content arbitrarily difficult and is a wast of students time.
