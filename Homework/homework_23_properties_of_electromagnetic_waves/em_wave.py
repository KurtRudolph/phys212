from sympy import *
from math import *
mu_0 = 4. * pi * 10.*(-7)
t = 1.5 * 10.**(-9)
c = 299792458.
I = 45.0
lambd = 0.3
omega = 2. * pi * c / lambd
Z_0 = mu_0 * c
B_0 = (2 * Z_0 * I)**(1/2) / c
print( B_0 * cos( - omega * t))

# What I put in my calculator 
# (2*4*pi*10^(-7)*c*45)/c*cos(-2*pi*c/.3*1.5*10^(-9))^(1/2)
print((2.*4.*pi*10.**(-7)*c*45.)/c*cos(-2.*pi*c/.3*1.5*10.**(-9))**(1/2))