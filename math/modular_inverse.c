#include <stdio.h>

/* Compute the modular multiplicative inverse of x modulo p */
int modular_inverse( int x, int p );
int modular_inverse( int x, int p )
{
    int inverse = 0;

    for ( int lastx = 1, lasty = 0, r, temp = 1; (r = x % p) != 0; x = p, p = r) {
        int quotient = x / p, tx = lastx, ty = lasty;
        lastx = inverse;
        lasty = temp;
        inverse = tx - quotient * inverse;
        temp = ty - quotient * temp;
    }
    return inverse;

}

int main( void )
{
    printf( "%d\n", modular_inverse( 3, 11 ) );
    return 0;
}

