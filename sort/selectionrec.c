#include <stdio.h>

/* Selection sort recursive version, sort the subarray a[start..end-1] */
void selection( int a[], int begin, int end );
void selection( int a[], int begin, int end )
{
    if ( begin != end - 1 ) {
        int min = begin;
        for ( int i = begin + 1; i < end; ++i ) {
            if ( a[ i ] < a[ min ] )
                min = i;
        }
        int tmp = a[ begin ];
        a[ begin ] = a[ min ];
        a[ min ] = tmp;
        selection( a, begin + 1, end );
    }
}

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 };

    selection( a, 0, 5 );
    for ( int i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
