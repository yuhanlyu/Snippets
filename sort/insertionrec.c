#include <stdio.h>

void insertion( int a[], int n );

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    insertion( a, 5 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void insertion( int a[], int n )
{
    int     i, tmp;

    if ( n != 0 ) {
        insertion( a, n - 1 );
        for ( tmp = a[ n - 1 ], i = n - 1; i > 0 && a[ i - 1 ] > tmp; --i )
            a[ i ] = a[ i - 1 ];
        a[ i ] = tmp;
    }
}

