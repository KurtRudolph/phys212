from sympy import *

V = 12.0
mu = 10**-6
r_1 = 110.0
r_2 = 220.0
r_3 = 330.0
c_1 = 40.0 * mu
c_2 = 80.0 * mu

r_equiv = r_1 + 1/(1/r_2 + 1/r_3)

c_equiv = 1/(1/c_1 + 1/c_2)

print( ((r_2 * V)/(r_1 + r_2))/(1/c_1 + 1/c_2))
