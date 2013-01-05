#include <stdio.h>

int main( void )
{
    int     n, i, j, f;

    scanf( "%d", &n );
    for ( i = f = 0; i >= 0; f == 0 ? ++i : --i ) {
        if ( i == n / 2 ) {
            f = 1;
            if ( n % 2 == 1 ) {
                for ( j = 0; j < i; ++j )
                    putchar( ' ' );
                puts( "*" );
            }
            continue;
        }
        for ( j = 0; j < i; ++j )
            putchar( ' ' );
        for ( j = 0; j < n - i * 2; ++j )
            putchar( '*' );
        puts( "" );
    }
    return 0;
}

