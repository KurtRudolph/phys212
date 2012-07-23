from sympy import *

L = 340. * 10**-3
C = 25. * 10**-6
R = 280.
V_L = 60.6
V_C = -10.1

omega = sqrt( abs( V_L / (L * C * V_C)))
omega = 840.168
X_L = omega * L
X_C = 1 / (omega * C)

sigma = atan( (X_L - X_C) / R)

t = sigma / omega

print( t)