#include <stdio.h>
                                                                                
/* This function compute the greatest common divisor of two positive 
 * integers p and q */
unsigned int gcd( unsigned int p, unsigned int q );
unsigned int gcd( unsigned int p, unsigned int q )
{
    if ( q != 0 ) {
        while ( ( p %= q ) && ( q %= p ) )
            ;
    }		
    return p + q;
}

int main( void )
{
    printf( "GCD of 5 and 7 should be 1. gcd(5, 7) = %u\n", gcd( 5, 7 ) );
    printf( "GCD of 54 and 24 should be 6. gcd(54, 24) = %u\n", gcd( 54, 24 ) );
    return 0;
}
