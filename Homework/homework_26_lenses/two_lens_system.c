#include <stdio.h>
#include <math.h>

#define PI 3.1415968

int main( ){

double  x_2 = -.169,
        y_2 = .021,
        f   = -.422;

//1)
double x_1 = -1 / (1 / f - 1 / x_2);
printf( "x_1 = %lf\n", x_1 * 100);

//2)
double y_1 = x_1 * y_2 / x_2;
printf( "y_1 = %lf\n", y_1 * 100);

//3)
double x_3 = -.172;
double f_converging = .0815;
double x_4 = 1 / ( 1 / f_converging - 1 / (x_3 - x_1)) + x_3;
printf( "x_4 = %lf\n", x_4 * 100);

//4)
double x_5 = 1 / (1 / f + 1 / x_4);
printf( "x_5 = %lf\n", x_5 * 100);


return 0;
}
