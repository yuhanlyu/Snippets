#include <stdio.h>
                                                                                
/* This function computes the greatest common divisor of two positive 
 * integers num1 and num2 */
unsigned int gcd( unsigned int num1, unsigned int num2 );
unsigned int gcd( unsigned int num1, unsigned int num2 )
{
    /* Euclid's algorithm */
    while ( ( num1 %= num2 ) && ( num2 %= num1 ) )
        ;
    return num1 + num2;
}

int main( void )
{
    printf( "GCD of 5 and 7 should be 1. gcd(5, 7) = %u\n", gcd( 5, 7 ) );
    printf( "GCD of 54 and 24 should be 6. gcd(54, 24) = %u\n", gcd( 54, 24 ) );
    return 0;
}
