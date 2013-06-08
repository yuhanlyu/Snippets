#include <stdio.h> 
#include <string.h>

/* Sieve of Eratosthenes */
int sieve( int n, int primes[] );
int sieve( int n, int primes[] )
{
    char    is_prime[ n + 1 ];
    int     count = 0;

    memset( is_prime, 1, (n + 1) * sizeof(char) );

    for ( int i = 2; i * i <= n; ++i )
        if ( is_prime[ i ] == 1 )
            /* Scan backward to improve performance
             * See Algorithms Unplugged */
            for ( int k = (n - 1) / i, j = i * k; k >= i; --k, j -= i )
                if ( is_prime[ k ] == 1 )
                    is_prime[ j ] = 0;

    for ( int i = 2; i <= n; ++i )
        if ( is_prime[ i ] == 1 )
            primes[ count++ ] = i;
    return count;
}

int main( void )
{
    int     primes[ 100000 ];
    printf( "%d\n", sieve( 1000000, primes ) );
    return 0;
}
