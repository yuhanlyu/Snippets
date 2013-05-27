#include <stdio.h>

void mergesort( int a[], int left, int right );
void merge( int a[], int left, int mid, int right );

/* Merge sort: sort the array a from a[left] to a[right - 1] */
void mergesort( int a[], int left, int right )
{
    if ( left < right - 1 ) {
        int     mid = left + ( right - left )/2;

        mergesort( a, left, mid);
        mergesort( a, mid, right );
        merge( a, left, mid, right );
    }
}

/* Merge: Merge two sorted array a[left .. mid - 1], a[mid .. right - 1] */
void merge( int a[], int left, int mid, int right )
{
    int     aux[ right - left ];

    for ( int i = left, j = mid, k = 0; k < right - left; ++k ) {
        if ( i == mid ) {
            aux[ k ] = a[ j++ ];
        } else if ( j == right ) {
            aux[ k ] = a[ i++ ];
        } else
            aux[ k ] = a[ i ] < a[ j ] ? a[ i++ ] : a[ j++ ];
    }
    for ( int i = 0, j = left; j < right; ++i, ++j )
        a[ j ] = aux[ i ];
}

int main( void )
{
    int     a[ 6 ] = { 1, 5, 3, 2, 4, 6 };

    mergesort( a, 0, 6 );
    for ( int i = 0; i < 6; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
