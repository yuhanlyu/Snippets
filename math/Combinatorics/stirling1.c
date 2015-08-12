#include <stdio.h>

int Stirling1( int n, int k );

int main( void )
{
    int     n, k;

    while ( scanf( "%d %d", &n, &k ) == 2 )
        printf( "%d\n", Stirling1( n, k ) );
    return 0;
}

int Stirling1( int n, int k )
{
    if ( n < k )
        return 0;
    if ( k == 0 )
        return n == 0;
    return ( n - 1 ) * Stirling1( n - 1, k ) + Stirling1( n - 1, k - 1 );
}

