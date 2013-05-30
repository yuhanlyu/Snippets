#include <stdio.h>

/* Ackermann Function */
int Ackermann( int m, int n );
int Ackermann( int m, int n )
{
    if ( m == 0 )
        return n + 1;
    if ( n == 0 )
        return Ackermann( m - 1, 1 );
    return Ackermann( m - 1, Ackermann( m, n - 1 ) );
}

int main( void )
{
    for ( int m, n; scanf( "%d %d", &m, &n ) == 2; )
        printf( "%d\n", Ackermann( m, n ) );
    return 0;
}

