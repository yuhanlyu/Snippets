#include <stdio.h>

int main( void )
{
    int     n;

    while ( scanf( "%d", &n ) == 1 )
        printf( "%3.0f  %6.1f\n", (double)n, ( 9.0 * n ) / 5.0 + 32.0 );
    return 0;
}

