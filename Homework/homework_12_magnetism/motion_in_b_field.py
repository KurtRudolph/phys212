from sympy import * 
from mpmath import *

m = 1.67 * 10.0**(-27)
q = 1.6 * 10.0**(-19)
v = 1.0 * 10.0**(6)
B = 1.2
k = 1.0/2.0 * m * v**2
r = (2.0 * m * k/(q * B)**2)**(1.0/2.0)

d = pi * r

t = d/v
print( t)
