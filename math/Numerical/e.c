#include <stdio.h>
#include <math.h>

int main( void )
{
    double  e, tmp = 0.0;
    int     i, n;

    for ( e = 1.0, n = i = 1; fabs( e - tmp ) > 0.0000001; ++i, n *= i ) {
        tmp = e;
        e += 1.0 / n;
    }
    printf( "%f\n", e );
    return 0;
}

