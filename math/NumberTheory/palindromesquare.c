#include<stdio.h>

// Find palindromic squares
int main( void )
{
    int     a[ 10 ], n, t, i, j;

    for ( n = 1; n < 1000; ++n ) {
        t = n * n;
        for ( i = 0; t != 0; ++i, t /= 10 )
            a[ i ] = t % 10;
        for ( j = 0, --i; j < i; ++j, --i )
            if ( a[ i ] != a[ j ] )
                break;
        if ( j >= i )
            printf( "%d\n", n * n );
    }
    return 0;
}

