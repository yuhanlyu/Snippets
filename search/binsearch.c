#include <stdio.h>

/* Find the index of x in a sorted array v with length n > 0 */
int binsearch( int x, const int v[], int n );
int binsearch( int x, const int v[], int n )
{
    for ( int low = 0, high = n - 1; low <= high; ) {
        int mid = low + ((high - low) / 2);
        if ( v[ mid ] < x )
            low = mid + 1;
        else if ( v[ mid ] > x )
            high = mid - 1;
        else
            return mid;
    }
    return -1;
}

int main( void )
{
    int     a[ 6 ] = { 0, 1, 3, 5, 7, 9 };

    printf( "%d\n", binsearch( -1, a, 6 ) );
    printf( "%d\n", binsearch( 0, a, 6 ) );
    printf( "%d\n", binsearch( 1, a, 6 ) );
    printf( "%d\n", binsearch( 2, a, 6 ) );
    printf( "%d\n", binsearch( 3, a, 6 ) );
    printf( "%d\n", binsearch( 4, a, 6 ) );
    printf( "%d\n", binsearch( 5, a, 6 ) );
    printf( "%d\n", binsearch( 6, a, 6 ) );
    printf( "%d\n", binsearch( 7, a, 6 ) );
    printf( "%d\n", binsearch( 8, a, 6 ) );
    printf( "%d\n", binsearch( 9, a, 6 ) );
    printf( "%d\n", binsearch( 10, a, 6 ) );
    return 0;
}
