#include <stdio.h>

int Stirling2( int n, int k );

int main( void )
{
    int     n, k;

    while ( scanf( "%d %d", &n, &k ) == 2 )
        printf( "%d\n", Stirling2( n, k ) );
    return 0;
}

int Stirling2( int n, int k )
{
    if ( n < k )
        return 0;
    if ( k == 0 )
        return n == 0;
    return k * Stirling2( n - 1, k ) + Stirling2( n - 1, k - 1 );
}

