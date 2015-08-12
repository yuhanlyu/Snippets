#include <stdio.h>

int catalan( int n );

int main( void )
{
    int     n;

    while ( scanf( "%d", &n ) == 1 )
        printf( "%d\n", catalan( n ) );
    return 0;
}

int catalan( int n )
{
    int     i, result = 1;

    for ( i = 1; i < n; ++i )
        result = result * ( 4 * i + 2 ) / ( i + 2 );
    return result;
}

