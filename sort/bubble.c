#include <stdio.h>

/* Bubble sort */
void bubble( int a[], int n );
void bubble( int a[], int n )
{
    for ( int i = 0; i < n - 1; ++i )
        for ( int j = n - 1; j > i; --j )
            if ( a[ j - 1 ] > a[ j ] ) {
                int t = a[ j ]; 
                a[ j ] = a[ j - 1 ]; 
                a[ j - 1 ] = t;
            }
}

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    bubble( a, 5 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
