#include<stdio.h>

// Test Lagrange's four-square theorem
int main( void )
{
    int     n, i, j, k, h;

BEGIN:
    while ( scanf( "%d", &n ) == 1 ) {
        for ( i = 1; i < n / 2; ++i )
            for ( j = 0; j <= i; ++j )
                for ( k = 0; k <= j; ++k )
                    for ( h = 0; h <= k; ++h )
                        if ( i * i + j * j + k * k + h * h == n ) {
                            printf( "%d = %d*%d + %d*%d + %d*%d + %d*%d\n",
                                    n, i, i, j, j, k, k, h, h );
                            goto BEGIN;
                        }
    }
    return 0;
}
