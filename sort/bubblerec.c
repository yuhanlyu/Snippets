#include <stdio.h>
#define MAX 10

void bubble( int a[], int n );

void bubble( int a[], int n )
{
    int     i, t;

    if ( n == 1 )
        return;
    for ( i = 0; i < n - 1; ++i )
        if ( a[ i ] > a[ i + 1 ] ) {
            t = a[ i ];
            a[ i ] = a[ i + 1 ];
            a[ i + 1 ] = t;
        }
    bubble( a, n - 1 );
}

int main( void )
{
    int     a[ MAX ] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 }, i;

    bubble( a, MAX );
    for ( i = 0 ; i < MAX; ++i )
        printf( "%d ", a[ i ] );
    puts( "" );
    return 0;
}
