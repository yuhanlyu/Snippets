#include <stdio.h>

void selection( int a[], int start, int n );

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    selection( a, 0, 5 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void selection( int a[], int start, int n )
{
    int     i, min, tmp;

    if ( start != n - 1 ) {
        for ( min = start, i = start + 1; i < n; ++i )
            if ( a[ i ] < a[ min ] )
                min = i;
        tmp = a[ start ];
        a[ start ] = a[ min ];
        a[ min ] = tmp;
        selection( a, start + 1, n );
    }
}

