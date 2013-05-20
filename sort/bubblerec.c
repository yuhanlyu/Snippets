#include <stdio.h>

/* Bubble sort */
void bubble( int a[], int n );
void bubble( int a[], int n )
{
    if ( n == 1 )
        return;
    for ( int i = 0; i < n - 1; ++i ) {
        if ( a[ i ] > a[ i + 1 ] ) {
            int t = a[ i ];
            a[ i ] = a[ i + 1 ];
            a[ i + 1 ] = t;
        }
    }
    bubble( a, n - 1 );
}

int main( void )
{
    int     a[ 10 ] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

    bubble( a, 10 );
    for ( int i = 0 ; i < 10; ++i )
        printf( "%d ", a[ i ] );
    puts( "" );
    return 0;
}
