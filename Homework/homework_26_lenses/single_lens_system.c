#include <stdio.h>
#include <math.h>

#define PI 3.1415968

int main( ){

  double  x_1 = -.67,
          x_2 = 1.093,
          y_1 = .0446,
          n   = 1.61;
//1)
  double f_lens = 1 / (-1 / x_1 + 1 / x_2);
  printf( "f_lens = %lf\n", f_lens * 100);

//2)
  double y_2 = y_1 * x_2 / (-x_1);
  printf( "y_2 = %lf\n", -y_2 * 100);

//3)
  double R = (n - 1) * f_lens;
  printf( "R = %lf\n", R * 100);

//4)
  double x_1_new = -.233;
  double x_2_new = 1 / (1 / f_lens + 1 / x_1_new);
  printf( "x_2_new = %lf\n", x_2_new * 100);

return 0;
}