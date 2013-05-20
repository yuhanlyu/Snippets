#include <stdio.h>

void quick( int a[], int left, int right );
int  partition( int a[], int left, int right );

int main( void )
{
    int     a[ 5 ] = { 5, 4, 3, 2, 1 }, i;

    quick( a, 0, 4 );
    for ( i = 0; i < 5; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}

void quick( int a[], int left, int right )
{
    int     pivot;

    if ( right > left ) {
        pivot = partition( a, left, right );
        quick( a, left, pivot - 1 );
        quick( a, pivot + 1, right );
    }
}

int  partition( int a[], int left, int right )
{
    int     i, pivot = a[ right ], store = left, tmp;

    for ( i = left; i < right; ++i )
        if ( a[ i ] <= pivot ) {
            tmp = a[ store ];
            a[ store ] = a[ i ];
            a[ i ] = tmp;
            ++store;
        }
    a[ right ] = a[ store ];
    a[ store ] = pivot;
    return store;
}

