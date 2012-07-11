from sympy import * 
from mpmath import *
mu = 10.0**(-6)
m = 7.5 * 10.0**(-8)
B = 1.9
t = 481.0 * mu
r = 0.5
d = pi/2.0 * r


# 1)
v = d/t
print( v)

# 2)
ke = 1.0/2.0 * m * v**2
t_1 = 160.3 * mu

percent_d_traveled = t_1/t

d * percent_d_traveled 

q = symbols( 'q')

q = solve( m * v/(q * B) - r, q)[0]

print( q * v * B * percent_d_traveled)


# 4)
print(q/mu)
