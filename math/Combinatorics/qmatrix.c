#include <stdio.h>
#define MAX 7

void mult( int a[][2], int b[][2], int c[][2] );

int main( void )
{
    int     qmatrix[ MAX ][ 2 ][ 2 ] = { { { 0 } } };
    int     i, n;

    qmatrix[0][1][1] = 0;
    qmatrix[0][1][0] = qmatrix[0][0][1] = qmatrix[0][0][0] = 1;
    for ( i = 1; i < MAX; ++i )
        mult( qmatrix[i], qmatrix[i-1], qmatrix[i-1] );

    while ( scanf( "%d", &n ) == 1 ) {
        int     tmp[2][2] = { { 1, 0 }, { 0, 1 } };

        for ( i = 0; n != 0; ++i, n >>= 1 )
            if ( ( n & 1 ) > 0 )
                mult( tmp, tmp, qmatrix[ i ] );
        printf( "%d\n", tmp[0][1] );
    }
    return 0;
}

void mult( int a[][2], int b[][2], int c[][2] )
{
    int     t[4];

    t[0] = b[0][0] * c[0][0] + b[0][1] * c[1][0];
    t[1] = b[0][0] * c[1][0] + b[0][1] * c[1][1];
    t[2] = b[1][0] * c[0][0] + b[1][1] * c[1][0];
    t[3] = b[1][0] * c[1][0] + b[1][1] * c[1][1];
    a[0][0] = t[0];
    a[0][1] = t[1];
    a[1][0] = t[2];
    a[1][1] = t[3];
}

