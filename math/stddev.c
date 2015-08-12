#include <stdio.h>
#include <math.h>

int main( void )
{
    int     n;
    double  x, sum, sum2;

    for ( sum = sum2 = n = 0; scanf( "%lf", &x ) == 1; ++n ) {
        sum += x;
        sum2 += x * x;
    }
    printf( "%.4f\n", sqrt( ( sum2 - sum * sum / n ) / ( n - 1 ) ) );
    return 0;
}

