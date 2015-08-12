#include <stdio.h>

int phi( int n );

int main( void )
{
    int     n;

    while ( scanf( "%d", &n ) == 1 )
        printf( "%d\n", phi( n ) );
    return 0;
}

// Euler's totient function
int phi( int n )
{
    int     i, result = n;

    for ( i = 2; i * i <= n; ++i )
        if ( n % i == 0 ) {
            result = result / i * ( i - 1 );
            do
                n /= i;
            while ( n % i == 0 );
        }
    return n != 1 ? result / n * ( n - 1 ) : result;
}

