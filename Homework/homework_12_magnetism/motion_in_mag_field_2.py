from sympy import * 
from mpmath import *
from math import *

mu = 10.0**(-6)


q = 1.6 * 10**(-19)
m = 1.67 * 10**(-27)

D = d = 0.52

v_x_f = 4.3 * 10**5
v_y_f = 1.6 * 10**5

# 1)
v_x_0 = sqrt( v_x_f**2 + v_y_f**2)

print( v_x_0)

# 2)
theta = acos( v_x_f / v_x_0)

F_B, B, R, w = symbols( 'F_B B R w')

print( solve( ( 
        m * v_x_0 / (q * B) - R,
        v_x_0 / R - w,
        v_x_0**2 / R - R * w**2
        ), w, B, R))


