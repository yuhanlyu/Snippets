#include <stdio.h>

int main( void )
{
    int     n, i, f, count;

    while ( scanf( "%d", &n ) == 1 && n != 0 ) {
        int     output[ 10 ] = { 0 };

        for ( count = 1 << n, f = 0; count > 0; --count, f = !f ) {
            for ( i = 0; i < n; ++i )
                printf( "%d ", output[ i ] );
            puts( "" );
            if ( f == 0 )
                output[ n - 1 ] = !output[ n - 1 ];
            else {
                for ( i = n - 1; i > 0; --i )
                    if ( output[ i ] == 1 )
                        break;
                output[ i - 1 ] = !output[ i - 1 ];
            }
        }
    }
    return 0;
}

