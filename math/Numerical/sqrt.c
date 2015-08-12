#include <stdio.h>

int main( void )
{
    double  a, x0 = 0.0, x1 = 1.0;

    scanf( "%lf", &a );
    /* Newton's method */
    while ( x0 != x1 ) {
        x0 = x1;
        x1 = 0.5 * ( x1 + a / x1 );
    }
    printf( "%f\n", x1 );
    return 0;
}

