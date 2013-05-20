#include <stdio.h>

void heapsort( int a[], int n );
void fixDown( int a[], int k, int n );

int main( void )
{
    int     a[ 6 ] = { 6, 5, 4, 3, 2, 1 }, i;

    heapsort( a, 6 );
    for ( i = 0; i < 6; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void heapsort( int a[], int n )
{
    int     i, tmp;

    for ( --a, i = n / 2; i >= 1; --i )
        fixDown( a, i, n );
    while ( n > 1 ) {
        tmp = a[ 1 ];
        a[ 1 ] = a[ n ];
        a[ n ] = tmp;
        fixDown( a, 1, --n );
    }
}

void fixDown( int a[], int k, int n )
{
    int     j, tmp;

    while ( 2 * k <= n ) {
        j = 2 * k;
        j += ( j < n && a[ j ] < a[ j + 1 ] );
        if ( a[ k ] >= a[ j ] )
            break;
        tmp = a[ k ];
        a[ k ] = a[ j ];
        a[ j ] = tmp;
        k = j;
    }
}

