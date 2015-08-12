#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100

int main( void )
{
    int     n, k, i, r;

    srand( time( NULL ) );
    while ( scanf( "%d %d", &n, &k ) == 2 ) {
        int     array[ MAX ] = { 0 };

        for ( i = n - k; i < n; ++i ) {
            r = rand() % i;
            if ( array[ r ] == 1 )
                array[ i ] = 1;
            else
                array[ r ] = 1;
        }
        for ( i = 0; i < n; ++i )
            if ( array[ i ] == 1 )
                printf( "%d ", i );
        puts( "" );
    }
    return 0;
}

