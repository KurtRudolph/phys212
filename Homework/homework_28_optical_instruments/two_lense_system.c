#include <stdio.h>
#include <math.h>

int main( ){
  double  x_3 = .579,
          f_1 = .125,
          x_2 = .258,
          x_0 = -.366,
          y_0 = .121;

  double x_1 = -1 / (1 / f_1 - 1 / x_0);
  printf( "x_1 = %lf\n", x_1 * 100);

  double y_1 = x_1 * y_0 / x_0;
  printf( "y_1 = %lf\n", y_1 * 100);

  double f_2 = - 1 / (1 / (x_1 - x_2) - 1 / ( x_3 - x_2));
  printf( "f_2 = %lf\n", f_2 * 100);

  double y_3 = (x_3 + x_2) * y_1 / (x_1 - x_2);
  printf( "y_1 = %lf\n", y_1 * 100);
  

return 0;
}
