from sympy import *
from mpmath import *

d = .08
I = 0.25
B = 1.3


A = sqrt(3) * d**2/4
mu = I * A

print(- mu * B * cos( radians(180)))
