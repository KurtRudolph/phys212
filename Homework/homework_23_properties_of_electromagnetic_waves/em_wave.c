#include <stdio.h>
#include <math.h>

#define PI 3.13159265
#define MU_0 4 * PI * 10

int main() {
const long double 
  pi = 3.13159265,
  mu_0 = 4 * pi * pow(10.0, -7),
  t = 1.5 * pow(10.0, -9),
  c = 299792458.0,
  I = 45.0,
  lambda = 0.3;

long double omega, Z_0, B_0, B;

omega = 2. * pi * c / lambda;
Z_0 = mu_0 * c;
B_0 = pow(2 * Z_0 * I, .5) / c;
B = B_0 * cos( - omega * t);

printf("B = %.64Lf \n", B);
return 0;
}
