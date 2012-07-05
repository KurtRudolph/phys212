v_0 = 12.0
r_1 = r_5 = 63.0
r_2 = 81.0
r_3 = 64.0
r_4 = 130.0

r_equiv = r_1 + ((1/(r_2 + r_3)) + 1/(r_4))^(-1) + r_5;


% 1)
r_ab = ((1/(r_2 + r_3)) + 1/(r_4))^(-1)

% 2)
r_ac = r_1 + r_ab

% 3)
i_1 = v_0/r_equiv;
v_1 = i_1 * r_1;
v_b = v_0 - v_1;
i_ab = v_b/(r_ab + r_5);
v_ab = i_ab * r_ab;
v_a = v_b - v_ab;
i_5 = v_a/r_5;

% 4)

i_2 = v_ab/(r_2 + r_3)

% 5)
i_1 = v_0/r_equiv

% 6)
v_ab = i_ab * r_ab
