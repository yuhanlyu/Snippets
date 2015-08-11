#include <stdio.h>

int main( void )
{
    int     i;
    double  x, avg = 0.0, sum = 0.0;

    for ( i = 1; scanf( "%lf", &x ) == 1; ++i ) {
        avg += ( x - avg ) / i;
        sum += x;
    }
    printf( "%f %f\n", avg, sum );

    return 0;
}

