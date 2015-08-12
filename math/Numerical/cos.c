#include <stdio.h>
#include <math.h>

int main( void )
{
    double  cosine = 1.0, radius, power, previous = 0.0, factorial = 2.0;
    int     n = 3, flag = -1;

    scanf( "%lf", &radius );
    for ( power = pow( radius, 2.0 );
            fabs( cosine - previous ) > 0.0000001;
            factorial *= n * ( n + 1 ), n += 2, power *= radius * radius ) {
        previous = cosine;
        cosine += power / factorial * flag;
        flag = -flag;
    }
    printf( "%f %f\n", cosine, cos( radius ) );
    return 0;
}

