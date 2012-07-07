from sympy import *

V = 12.0
v_b = 11.8
r_1 = r_3 = 43.0
r_4 = r_5 = 84.0
r_2 = 150.0

i_1, i_2, i_3, i_4, i_5, r = symbols('i_1 i_2 i_3 i_4 i_5 r')

# 1) What is i_1, the current that flows through the resistor r_1?

r_equiv = r_1 + 1/(1/r_2 + 1/(r_3 + r_4 + r_5)) 

print( solve( V - (V * r)/(r_equiv) - v_b, r))

# Yup still haven't figured out how to grab values from solve, first time using python gime a break...
r = 2.17788550323176

i_1 = V/(r_equiv + r)
print( 1000 * i_1)

# 2) What is r, the internal resistance of the battery?

r_fuck_it_wont_accept_the_other_r = symbols('r_fuck_it_wont_accept_the_other_r')

print( solve( V - i_1 * r_fuck_it_wont_accept_the_other_r - v_b, r_fuck_it_wont_accept_the_other_r))

# 3) What is i_3, the current through resistor r_3?

print( solve( (i_3 + i_2 - i_1,
              r_2 * i_2 - r_3 * i_3 - r_4 * i_4 - r_5 * i_5,
              i_3 - i_4,
              i_3 - i_5,
              ), i_2, i_3, i_4, i_5))

# 4)
i_2 = 0.0527948572971549

print(i_2 * i_2 * r_2)

# 5)
print( i_2 * r_2)
