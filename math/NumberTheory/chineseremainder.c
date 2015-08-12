#include <stdio.h>

// Chinese remainder theorem
int main( void )
{
    int     a, p, b, q, inverse, temp;

    scanf( "%d %d %d %d", &a, &p, &b, &q );
    inverse = GFInverse( q, p % q );
    temp = ( b - a % q ) * inverse % q;
    printf( "%d\n", temp * p + a );
    return 0;
}

