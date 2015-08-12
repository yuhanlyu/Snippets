#include <stdio.h>

int main( void )
{
    int     a, b, n, d, x, y, i;

    scanf( "%d %d %d", &a, &b, &n );
    d = ExtendedGCD( a, n, &x, &y );
    if ( b % d == 0 ) {
        x = ( x * ( b / d ) ) % n;
        for ( i = 0; i < d; ++i )
            printf( "%d ", ( n + x + i * ( n / d ) ) % n );
        puts( "" );
    }
    return 0;
}

