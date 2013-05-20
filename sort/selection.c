#include <stdio.h>

void selection( int a[], int n );

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    selection( a, 5 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void selection( int a[], int n )
{
    int     i, j, min, tmp;

    for ( i = 0; i < n - 1; ++i ) {
        for ( min = i, j = i + 1; j < n; ++j )
            if ( a[ j ] < a[ min ] )
                min = j;
        tmp = a[ i ];
        a[ i ] = a[ min ];
        a[ min ] = tmp;
    }
}

