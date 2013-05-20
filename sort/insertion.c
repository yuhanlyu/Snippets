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
    int     i, j, tmp;

    for ( i = 1; i < n; ++i ) {
        for ( tmp = a[ i ], j = i; j > 0 && a[ j - 1 ] > tmp; --j )
            a[ j ] = a[ j - 1 ];
        a[ j ] = tmp;
    }
}

