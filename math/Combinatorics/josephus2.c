#include <stdio.h>
#define MAX 10000

int main( void )
{
    int     next[ MAX ], i, n, m, count, previous, dead;

    scanf( "%d %d", &n, &m );
    for ( i = 0; i < n; ++i )
        next[ i ] = ( i + 1 ) % n;
    for ( dead = i = 0, count = 1; dead != n - 1; i = next[ i ], ++count ) {
        if ( count == m ) {
            next[ previous ] = next[ i ];
            count = 0;
            ++dead;
        }
        previous = i;
    }
    printf( "%d\n", i + 1 );
    return 0;
}

