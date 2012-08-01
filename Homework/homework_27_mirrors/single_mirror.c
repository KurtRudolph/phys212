#include <stdio.h>
#include <math.h>

#define PI 3.1415968

int main(){

  double  x_2 = -.91,
          x_1 = -1.27,
          y_1 = .0306;

//1)
  double f = fabs( 1 / (1 / x_1 + 1/x_2));
  printf( "f = %lf\n", f * 100);

//2)
  double y_2 = x_2 * y_1 / x_1;
  printf( "y_2 = %lf\n", -y_2 * 100);

//3)
  double x_image_new = -1.82
  
  return 0;
}