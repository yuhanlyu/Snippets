#include <stdio.h>

/* Extended Greatest Common Divisor */
/* return = GCD( a, b ) = ax + by */
int extended_gcd( int a, int b, int *x, int *y );
int extended_gcd( int a, int b, int *x, int *y )
{
    *x = 0;
    *y = 1;
    // r = ax + by
    for ( int lastx = 1, lasty = 0, r; (r = a % b) != 0; a = b, b = r) {
        int quotient = a / b, tx = lastx, ty = lasty;
        lastx = *x;
        lasty = *y;
        *x = tx - quotient * *x;
        *y = ty - quotient * *y;
    }
    return b;
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
