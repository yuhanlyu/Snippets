#include <stdio.h>

/* Selection sort recursive version, sort the subarray a[start..end-1] */
void selection( int a[], int start, int end );
void selection( int a[], int start, int end )
{
    if ( start != end - 1 ) {
        int min = start;
        for ( int i = start + 1; i < end; ++i ) {
            if ( a[ i ] < a[ min ] )
                min = i;
        }
        int tmp = a[ start ];
        a[ start ] = a[ min ];
        a[ min ] = tmp;
        selection( a, start + 1, end );
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
