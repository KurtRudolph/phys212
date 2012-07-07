from sympy import *

r_1 = 100
r_2 = 200
r_3 = 30
r_4 = 400
v_a = 4
v_b = 12

i_1, i_2, i_3 = symbols('i_1 i_2 i_3')


# i_1 * r_1 + i_3 * r_3 - v_1 = 0

# i_1 * r_1 + i_2 * r_2 - v_2 - v_1 = 0

# i_1 = i_2 + i_3


print( solve( (i_1 * r_1 + i_3 * r_3 - v_a, i_1 * r_1 + i_2 * r_2 - v_b - v_a, - i_1 + i_2 + i_3), i_1, i_2, i_3))

