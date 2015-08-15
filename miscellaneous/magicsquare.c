#include <stdio.h>
int A[ 100 ][ 100 ];

int main( void )
{
    int     n, x, y, number;

    while ( scanf( "%d", &n ) == 1 && n % 2 == 1 ) {
        for ( y = 0; y < n; ++y )
            for ( x = 0; x < n; ++x )
                A[ y ][ x ] = 0;
        y = 0;
        x = n / 2;
        A[ y ][ x ] = 1;
        for ( number = 2; number <= n * n; ++number ) {
            x = ( x + 1 ) % n;
            y = ( y - 1 + n ) % n;
            if ( A[ y ][ x ] != 0 ) {
                x = ( x - 1 + n ) % n;
                y = ( y + 2 ) % n;
            }
            A[ y ][ x ] = number;
        }
        for ( y = 0; y < n; ++y ) {
            for ( x = 0; x < n; ++x )
                printf( "%d ", A[ y ][ x ] );
            puts( "" );
        }
    }
    return 0;
}
