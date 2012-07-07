from sympy import *

r_1 = r_5 = 52.0
r_2 = r_6 = 93.0
r_3 = 41.0
r_4 = 107.0
v_a = 18 # V_1 in the image
v_b = 12 # V_2 in the image

i_1, i_2, i_3, i_4, i_5, i_6 = symbols('i_1 i_2 i_3 i_4 i_5 i_6')



# i_1 * r_1 + i_6 * r_6 - v_b + i_2 * r_2 = 0
# i_1 + i_3 - i_2 = 0

# i_5 * r_5 + i_4 * r_4 - v_b = 0
# i_1 * r_1 - v_a + i_3 * r_3 = 0
# i_3 * r_3 + i_2 * r_2 + i_5 * r_5 + i_4 * r_4 + i_6 * r_6 - v_a = 0

# i_2 * r_2 + i_3 * r_3 + v_a + i_6 * r_6 - v_b = 0



#print( solve( (
#                i_1 * r_1 + i_6 * r_6 - v_b + i_2 * r_2,
#                i_1 + i_3 - i_2,
#                i_2 * r_2 + i_3 * r_3 + v_a + i_6 * r_6 - v_b,
#                i_5 * r_5 + i_4 * r_4 + v_b,
#                i_1 * r_1 - v_a + i_3 * r_3,
#                i_3 * r_3 + i_2 * r_2 + i_5 * r_5 + i_4 * r_4 + i_6 * r_6 - v_a
#              ), i_1, i_2, i_3, i_4, i_5, i_6))


# 1)
print( solve( ( 
              i_4 * r_4 + i_5 * r_5 - v_b,
              (i_4 + i_5)/2 - i_4,
              ), i_5, i_4 ))

v_1 = i_1 * r_1
v_2 = i_2 * r_2
v_3 = i_3 * r_3
v_4 = i_4 * r_4
v_5 = i_5 * r_5

i_4 = i_5 = 0.0754716981132075

# 2) 3) 4) 
print( solve( (
              i_1 + i_3 - i_2,
              v_a + i_3 * r_3 - i_1 * r_1,
              v_b - i_2 * r_2 - i_3 * r_3 - v_a - i_6 * r_6,
              i_6 - i_2
              ), i_1, i_2, i_3, i_6 ))

# 5)
i_6 * r_6 # i_6 was found in the lat problem I just don't know how to use those computation yet.
