#include <stdio.h>
#include <math.h>

int main( void )
{
    int     n, q, d;

    while ( scanf( "%d %d", &n, &q ) == 2 ) {
        for ( d = 1; d <= n * ( q - 1 ); )
            d = (int)ceil( d * q / ( q - 1.0 ) );
        printf( "%d\n", q * n + 1 - d );
    }
    return 0;
}
