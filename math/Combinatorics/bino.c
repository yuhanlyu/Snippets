#include <stdio.h>

int Binomial( int n, int m );
int Binomial( int n, int m )
{
    if ( n == m || m == 0 )
        return 1;
    return Binomial( n - 1, m ) + Binomial( n - 1, m - 1 );
}

int main( void )
{
    int     n, m;

    while ( scanf( "%d %d", &n, &m ) == 2 )
        printf( "%d\n", Binomial( n, m ) );
    return 0;
}

