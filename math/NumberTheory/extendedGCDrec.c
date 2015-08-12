#include <stdio.h>

/* Extended Greatest Common Divisor recursive version */
/* return = GCD( a, b ) = ax + by */
int extended_gcd( int a, int b, int *x, int *y );
int extended_gcd( int a, int b, int *x, int *y )
{
    if ( b == 0 ) {
        *x = 1;
        *y = 0;
        return a;
    }
    int gcd = extended_gcd( b, a % b, y, x );
    *y -= ( a / b ) * *x;
    return gcd;
}

int main( void )
{
    int     x, y, gcd;

    gcd = extended_gcd( 120, 23, &x, &y );
    printf( "120 * %d + 23 * %d = %d\n", x, y, gcd );
    gcd = extended_gcd( 84, 33, &x, &y );
    printf( "84 * %d + 33 * %d = %d\n", x, y, gcd );
    return 0;
}

