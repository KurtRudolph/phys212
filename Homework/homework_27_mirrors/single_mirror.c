#include <stdio.h>
#include <math.h>

#define PI 3.1415968

int main(){

  double  x_2 = -.838,
          x_1 = -1.18,
          y_1 = .0546;

//1)
  double f = fabs( 1 / (1 / x_1 + 1/x_2));
  printf( "f = %lf\n", f * 100);

//2)
  double y_2 = x_2 * y_1 / x_1;
  printf( "y_2 = %lf\n", -y_2 * 100);

//3)
  double x_image_new_2 = -1.676;
  double x_image_new_1 = 1 / (1 / f + 1 / x_image_new_2);
  double y_image_new_2 = x_image_new_2 * y_1 / x_image_new_1;

  printf( "y_image_new_2 = %lf\n", y_image_new_2 * 100);

//4)
  double x_1_new = -.23;
  double y_1_new = y_1;

  double x_2_new = 1 / (1 / f + 1 / x_1_new);
  double y_2_new = x_2_new * y_1_new / x_1_new;

  printf( "y_2_new = %lf\n", -y_2_new * 100);
  
  return 0;
}