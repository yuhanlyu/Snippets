#include <stdio.h>

int gcd( int p, int q );

int main( void )
{
    return 0;
}

int gcd( int p, int q )
{
    return p % q == 0 ? q : gcd( q, p % q );
}
