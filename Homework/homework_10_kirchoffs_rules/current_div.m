v_0 = 10.0
r_a = r_b = r_c = r_1 = r_2 = 5

r_equiv = r_1 + ((1/(r_b + r_2)) + 1/(r_c))^(-1) + r_a;

r_alpha_beta = ((1/(r_b + r_2)) + 1/(r_c))^(-1)

i_1 = v_0/r_equiv
v_1 = i_1 * r_1;
v_alpha = v_0 - v_1;
i_alpha_beta = v_alpha/(r_alpha_beta + r_a);
v_alpha_beta = i_alpha_beta * r_alpha_beta;
v_beta = v_alpha - v_alpha_beta;

i_b = v_alpha_beta/(r_b + r_2)

v_b = i_b * r_b

v_2 = v_alpha_beta - v_b

i_2 = v_2/r_2

