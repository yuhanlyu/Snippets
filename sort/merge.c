#include <stdio.h>

void mergesort( int a[], int begin, int end );
void merge( int a[], int left, int mid, int right );

/* Merge sort: sort the array a[begin..end-1] */
void mergesort( int a[], int begin, int end )
{
    for ( int half_length = 1; half_length < end - begin; half_length *= 2 ) {
        for ( int left = begin, length = 2 * half_length; 
                  left <= end - half_length; left += length ) {
            int right = end < left + length ? end : left + length;
            merge( a, left, left + half_length, right );
        }
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
    int     a[ 6 ] = { 8, 3, 5, 6, 4, 2 };

    mergesort( a, 0, 6 );
    for ( int i = 0; i < 6; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
