from sympy import * 
from mpmath import *

mu = 10.0**(-6)
m = 7.5 * 10.0**(-8)
B = 1.9
t_f = 481.0 * mu
r = 0.5
d = pi/2.0 * r


# 1)
v = d/t_f
print( v)

# 2)
ke = 1.0/2.0 * m * v**2
t_1 = 160.3 * mu

percent_d_traveled = t_1/t_f

arc_length = d * percent_d_traveled 

theta = arc_length/r

q = symbols( 'q')

q = solve( m * v/(q * B) - r, q)[0]

print( q * v * cos( theta) * B)

# 3)
print( q * v * sin( theta) * B)

# 4)
print(q/mu)
