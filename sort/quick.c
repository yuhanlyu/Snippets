#include <stdio.h>

void quick( int a[], int begin, int end );
int  partition( int a[], int left, int right );

/* Quicksort: sort the array a[begin..end-1] */
void quick( int a[], int begin, int end )
{
    if ( begin < end - 1 ) {
        int pivot = partition( a, begin, end );
        quick( a, begin, pivot );
        quick( a, pivot + 1, end );
    }
}

/* In-place partition: partition the array a[left..right-1] with
 *                     the pivot a[right-1].
 *                     By using a[right-1] as the pivot, a[right-1]
 *                     is also a sentinel, such that simplifies the code */
int  partition( int a[], int left, int right )
{
    for ( int pivot = a[ right - 1 ], store = left; ; ++left ) {
        /* Termination condition */
        if ( left == right - 1 ) {
            a[ right - 1 ] = a[ store ];
            a[ store ] = pivot;
            return store;
        /* Swap element smaller than pivot to a[store] */
        } else if ( a[ left ] <= pivot ) {
            int tmp = a[ store ];
            a[ store++ ] = a[ left ];
            a[ left ] = tmp;
        }
    }
}

int main( void )
{
    int     a[ 5 ] = { 1, 3, 5, 2, 4 };

    quick( a, 0, 5 );
    for ( int i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
