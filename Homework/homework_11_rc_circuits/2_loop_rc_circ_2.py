from sympy import *
from mpmath import *

v = 12
mu = 10**-6
r_1 = r_2 = 43.0
r_3 = 112.0
r_4 = 104.0
c = 30 * mu


r_equiv_0 = r_1 + 1/(1/r_2 + 1/r_3) + r_4

# 1)

print( v/r_equiv_0)

# 2)

r_equiv_infty = r_1 + r_3 + r_4

print( r_3 * v/r_equiv_infty * c/mu)

# 3)

t = 548.0
q_0 = r_3 * v/r_equiv_infty * c
print( q_0 * e**(-t/(r_4 * c)) /mu)

# 4)
i_1, i_2, i_3 = symbols('i_1 i_2 i_3')

print( solve( (v/r_equiv_0 - i_1,
        i_1 - i_2 - i_3,
        r_2 * i_2 - r_3 * i_3
        ), i_1, i_2, i_3))
