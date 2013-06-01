#include <stdio.h>

/* Primality Test */
int is_primer( int n );
int is_primer( int n )
{
    if ( n == 2 )
        return 1;
    else if ( n == 0 || n % 2 == 0 )
        return 0;
    else
        for ( int i = 3; i * i <= n; i += 2 )
            if ( n % i == 0 )
                return 0;
    return 1;
}

int main( void )
{
    for ( int i = 2; i < 100; ++i )
        if ( is_primer( i ) )
            printf( "%d\n", i );
    return 0;
}
