#include <stdio.h>

// Compute a^b % n
int main( void )
{
    int     a, b, n, c, d, i;

    scanf( "%d %d %d", &a, &b, &n );
    for ( i = 0; b >> i > 0; ++i )
        ;
    for ( c = 0, d = 1; i >= 0; --i ) {
        c *= 2;
        d = ( d * d ) % n;
        if ( b >> i & 1 != 0 ) {
            ++c;
            d = ( d * a ) % n;
        }
    }
    printf( "%d\n", d );
    return 0;
}
