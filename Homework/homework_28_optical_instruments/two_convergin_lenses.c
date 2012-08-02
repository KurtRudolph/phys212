#include <stdio.h>
#include <math.h>

int main(){

  double  f_1 = 0.086,
          f_2 = .176,
          x_l2 = .5,
          x_0 = -.129,
          y_0 = .059;

  
  double x_1 = 1 / (1 / f_1 + 1 / (x_0));
  printf( "x_1 = %lf\n", x_1 * 100);

  double y_1 = x_1 * y_0 / x_0;
  printf( "y_1 = %lf\n", y_1 * 100);

  
  double x_3 = 1 / (1 / f_2 - 1 / (x_l2 - x_1)) + x_l2;
  printf( "x_3 = %lf\n", x_3 * 100);

  double y_3 = (x_3 - x_l2) * y_1 / (x_l2 - x_1) ;
  printf( "y_3 = %lf\n", y_3 * 100);
          
return 0;
}