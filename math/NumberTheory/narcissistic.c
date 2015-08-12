#include <stdio.h>

// Find narcissistic numbers
int main( void )
{
    int     i, d1, d2, d3;

    for ( i = 100; i < 1000; ++i ) {
        d1 = i / 100;
        d1 *= d1 * d1;
        d2 = ( i / 10 ) % 10;
        d2 *= d2 * d2;
        d3 = i % 10;
        d3 *= d3 * d3;
        if ( i == d1 + d2 + d3 )
            printf( "%d\n", i );
    }
    return 0;
}

