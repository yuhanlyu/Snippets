#include <stdio.h>

// Discrete logarithm
int main( void )
{
    int     m, n, i, t;

    while ( scanf( "%d %d", &m, &n ) == 2 ) {
        for ( i = 0, t = 1; m * t <= n; ++i, t *= m )
            ;
        printf( "%d\n", i );
    }
    return 0;
}

