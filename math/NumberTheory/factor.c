#include <stdio.h>

// Factor an integer
int main( void )
{
    int     n, i, c;

    while ( scanf( "%d", &n ) == 1 ) {
        printf( "%d = ", n );

        for ( i = 2; i <= n; ++i ) {
            if ( n % i == 0 ) {
                printf( "%d", i );
                for ( c = 0; n % i == 0; ++c )
                    n /= i;
                if ( c > 1 )
                    printf( "^%d", c );
                if ( n > 1 )
                    putchar( '*' );
            }
        }
        puts( "" );
    }
    return 0;
}

