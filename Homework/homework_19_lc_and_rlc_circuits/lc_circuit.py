from sympy import *

#U_E( t) = Q**2(t) / 2 * C

#U_B( t) = (1/2) * L * I^2(t)

#U_total = (1/2) * L * (I_max)^2
#U_total = (Q_max)**2 / 2 * C
#U_total = U_E + U_B

#U_B(0) = (1/2) U_total

#U_E(t) = Q**2(t) / 2 C
#U_B( t) = (1/2) L I^2( t)

#U_total = U_E( t) + U_B( t) = 2 U_B( 0)
mu = 10**(-6)
m = 10**(-3)
C = 0.05 * mu
L = 420 * m
I_0 = 75.0 * m

U_total = L * I_0**2

print( sqrt( U_total * 2 * C))