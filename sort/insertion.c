#include <stdio.h>

/* Insertion Sort */
void insertion( int a[], int n );
void insertion( int a[], int n )
{
    for ( int i = 1; i < n; ++i ) {
        int     j, tmp = a[ i ];
        for ( j = i; j > 0 && a[ j - 1 ] > tmp; --j )
            a[ j ] = a[ j - 1 ];
        a[ j ] = tmp;
    }
}

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 };

    insertion( a, 5 );
    for ( int i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
