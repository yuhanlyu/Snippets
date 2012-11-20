#include <stdio.h>
                                                                                
/* This function computes the n-th fibonacci number, where n should be a 
 * non-negative number */
unsigned int fibonacci( unsigned int n );
unsigned int fibonacci( unsigned int n )
{
    unsigned int even = 0, odd = 1, i;

    /* even is the i-th fibonacci number
       odd is the (i+1)-th fibonacci number */
    for ( i = 0; i < n; i += 2 ) {
        odd += even;
        even += odd;
    }
    return i == n ? even : odd;
}
                                                                                
int main( void )
{
    printf( "F20 should be 6765. fibonacci( 20 ) = %u\n", fibonacci( 20 ) );
    printf( "F31 should be 1346269. fibonacci( 31 ) = %u\n", fibonacci( 31 ) );

    return 0;
}
