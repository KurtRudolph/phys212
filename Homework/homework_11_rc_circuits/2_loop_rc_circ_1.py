from sympy import *

V = 24.0
mu = 10**-6
r_1 = r_2 = 75.0
r_3 = 64.0
r_4 = 61.0
c = 48.0 * mu

# 1)
r_equiv_0 = r_1 + r_4
print( V/r_equiv_0)

# 2)

r_equiv_infty = r_1 + r_2 + r_3 + r_4
print( V/r_equiv_infty)

# 3)
#solve( (q/c - r_2 * i_2 - r_3,
        

print( ((r_2 + r_3  ) * (V/r_equiv_infty)) * c / mu)

# 4)
r_5 = 51.0
r_equiv_0 = r_1 + 1/(1/r_5 + 1/(r_2 + r_3)) + r_4
print( V/r_equiv_0)

# 5)
# Same as 3) since there is no current when the resistor is full
print( ((r_2 + r_3  ) * (V/r_equiv_infty)) * c / mu)
