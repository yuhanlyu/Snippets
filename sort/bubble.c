#include <stdio.h>

void bubble( int a[], int n );

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    bubble( a, 5 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void bubble( int a[], int n )
{
    int     i, j, t;

    for ( i = 0; i < n - 1; ++i )
        for ( j = n - 1; j > i; --j )
            if ( a[ j - 1 ] > a[ j ] )
                t = a[j], a[j] = a[j-1], a[j-1] = t;
}

