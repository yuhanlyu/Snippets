#include <stdio.h>

/* Selection sort */
void selection( int a[], int n );
void selection( int a[], int n )
{
    for ( int i = 0, min = 0; i < n - 1; ++i, min = i ) {
        for ( int j = i + 1; j < n; ++j ) {
            if ( a[ j ] < a[ min ] )
                min = j;
        }
        int tmp = a[ i ];
        a[ i ] = a[ min ];
        a[ min ] = tmp;
    }
}

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 };

    selection( a, 5 );
    for ( int i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
