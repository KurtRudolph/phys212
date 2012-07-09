from sympy import *

v = 12
mu = 10**-6
r_1 = r_2 = 43.0
r_3 = 112.0
r_4 = 104.0
c = 30 * mu


r_equiv = r_1 + 1/(1/r_2 + 1/r_3) + r_4

# 1)

print( v/r_equiv)
