#include <stdio.h>
#define MAX 10

int main( void )
{
    int     a[ MAX ][ MAX ], i, j, k, n;

    while ( scanf( "%d", &n ) == 1 && n != 0 ) {
        for ( i = 0; i < n; ++i )
            for ( j = i, k = 1; k <= n; ++k, j = ( j + 1 ) % n )
                a[ i ][ j ] = k;
        for ( i = 0; i < n; ++i ) {
            for ( j = 0; j < n; ++j )
                printf( "%d ", a[ i ][ j ] );
            puts( "" );
        }
    }
    return 0;
}
