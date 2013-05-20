#include <stdio.h>

void merge( int a[], int left, int mid, int right );
void mergesort( int a[], int left, int right );

int main( void )
{
    int     a[ 6 ] = { 6, 5, 4, 3, 2, 1 }, i;

    mergesort( a, 0, 5 );
    for ( i = 0; i < 6; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void mergesort( int a[], int left, int right )
{
    int     i, m, min;

    for ( m = 1; m <= right - left; m += m )
        for ( i = left; i <= right - m; i += m + m ) {
            min = right < i + m + m - 1 ? right : i + m + m - 1;
            merge( a, i, i + m - 1, min );
        }
}

void merge( int a[], int left, int mid, int right )
{
    int     aux[ right - left + 1 ], i = left, j = mid + 1, k;

    for ( k = 0; k <= right - left; ++k ) {
        if ( i == mid + 1 ) {
            aux[ k ] = a[ j++ ];
            continue;
        } else if ( j == right + 1 ) {
            aux[ k ] = a[ i++ ];
            continue;
        } else
            aux[ k ] = a[ i ] < a[ j ] ? a[ i++ ] : a[ j++ ];
    }
    for ( i = 0, j = left; j <= right; ++i, ++j )
        a[ j ] = aux[ i ];
}

