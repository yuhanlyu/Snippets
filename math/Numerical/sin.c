#include <stdio.h>
#include <math.h>

int main( void )
{
    double  sine, radius, power, previous = 0.0, factorial = 6.0;
    int     n = 4, flag = -1;

    scanf( "%lf", &radius );
    for ( sine = radius, power = pow( radius, 3.0 );
            fabs( sine - previous ) > 0.0000001;
            factorial *= n * ( n + 1 ), n += 2, power *= radius * radius ) {
        previous = sine;
        sine += power / factorial * flag;
        flag = -flag;
    }
    printf( "%f\n", sine );
    return 0;
}

