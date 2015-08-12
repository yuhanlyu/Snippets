#include <stdio.h>

int main( void )
{
    int     a, b, c;

    while ( scanf( "%d %d", &a, &b ) == 2 ) {
        while ( b % a != 0 ) {
            c = b / a + 1;
            a = a * c - b;
            b *= c;
            printf( "%d ", c );
        }
        printf( "%d\n", b / a );
    }
    return 0;
}

