#include <stdio.h>

/* Fibonacci number */
int fibonacci( int n );
int fibonacci( int n )
{
    return n <= 1 ? n : ( fibonacci( n - 1 ) + fibonacci( n - 2 ) );
}

int main( void )
{
    for ( int i = 0; i <= 46; ++i )
        printf( "%d %d\n", i, fibonacci( i ) );
    return 0;
}
