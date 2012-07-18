from sympy import *
R_1 = 120.0
R_2 = 330.0
R_3 = 240.0

L = 1.6 * 10**(-3)

V = 9.0

# V = -L * dI/dt

# 63% is what the current will reach after one
# one time constant.

# I = I_f(1 - e^{t/\tau})

# Tau = L / R

# V - IR - L*dl/dt = 0

# Outer loop
## V - I1*R1 - I3*R3 - L*dI3/dt = 0

# Right Loop
## -I3*R3 - L*dI3/dt + I2R2 = 0

# I1 = I2 + I3

solve( (V - I_1 * R_1 - I_3 * R_3 - L * d_I_3 / d_t,
        -I_3 * R_3 - L* d_I_3 / d_t + I_2 * R_2,
        I_1 - I_2 - I_3
        V - I_3 * ((R_3 * R_1 + R_1 * R_2 + R_2 * R_3) / R_2) - (d_I_3 / d_t) * (L * ((R_1 + R_2) / R_2))

Tau = (L * (R_1 + R_2)) / (R_3 * R_1 + R_1 * R_2 + R_2 * R_3)