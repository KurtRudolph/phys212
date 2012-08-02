#include <stdio.h>
#include <math.h>

int main( ){ 

  double  x_2 = -.267,
          y_2 = .059,
          f   = .46;

  double x_1 = f * x_2 / ( x_2 - f) - f;
  printf( "x_1 = %lf\n", x_1 * 100);

  double y_1 = -x_1 * y_2 / x_2;
  printf( "y_1 = %lf\n", y_1 * 100);

  double x_2_new = x_2 / 2;
  double x_1_new = 1 / (1 / f - 1 / x_2_new);
  printf( "x_1_%lf\n", x_1_new * 100);
  

  double y_1_new = -x_1_new * y_2 / x_2_new;
  printf( "y_1_new = %lf\n", y_1_new * 100);

return 0;
}