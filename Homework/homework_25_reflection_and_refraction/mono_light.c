#include <stdio.h>
#include <math.h>

#define PI 3.14159265

int main () {
  double  phi_1 = 42.3 * PI/180,
          h     = .10,
          d     = .264;

  double d_hat = d - (h / tan( 30. * PI/180));
  printf( "d_hat = %fl\n", d_hat);


// 1)
  double phi_2 = atan( h / d_hat);
  printf( "phi_2 = %lf\n", phi_2 * 180/PI);

// 2)
  double n = sin( PI / 2 - PI / 6 -  phi_1) / sin( PI / 2 - PI / 6 - phi_2);
  printf( "n = %lf\n", n);

// 3)
  double phi_3 = PI / 2 - asin( n * sin( PI / 2 - phi_2));
  printf( "phi_3 = %lf\n", phi_3 * 180/PI);

// 4) 
  double phi_2_max = PI / 2 - asin( 1 / n);
  double phi_1_max  = PI / 3 - asin( n * sin( PI / 3 - phi_2_max));
  printf( "phi_1_max = %lf\n", phi_1_max * 180/PI);

// 5)
  double n_violet = 1.53;
  double phi_2_violet =  PI/3 - sin( PI/3 - phi_1) / n_violet;

  if( phi_2 > phi_2_violet)
    printf( "d_violet > d\n");
  else if( phi_2 < phi_2_violet)
    printf( "d_violet < d\n");
  else
    printf( "d_violet = d\n");

// 6)
  double phi_1_v = PI/3;
  double phi_2_v = PI/3 - asin( n_violet * sin( PI/3 - phi_1_v)) ;
  printf( "phi_2_v = %lf\n", phi_2_v * 180/PI);
  
  //sin( phi_3_v) = n * sin(phi_2_v)
  double phi_3_v =  PI/2 - asin( n_violet * sin( PI/2 - phi_2_v));
  printf( "phi_3 = %lf\n", phi_3_v * 180/PI);

  return 0;
}