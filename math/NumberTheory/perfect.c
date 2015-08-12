#include <stdio.h>

int is_perfect( int n );

int main( void )
{
    int     i;

    for ( i = 2; i < 1000; ++i )
        if ( is_perfect( i ) )
            printf( "%d\n", i );
    return 0;
}

// Testing perfect number
int is_perfect( int n )
{
    int     i, sum = 0;

    for ( i = 1; i < n; ++i )
        if ( n % i == 0 )
            sum += i;
    return sum == n;
}

