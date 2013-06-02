#include <stdio.h>
/* Extended GCD */
int egcd( int a, int b, int *x, int *y );
int egcd( int a, int b, int *x, int *y )
{
    int lastx = 1, lasty = 0, r;
    *x = 0;
    *y = 1;
    //r = ax + by
    for ( ; (r = a % b) != 0; a = b, b = r) {
        int quotient = a / b, tx = lastx, ty = lasty;
        lastx = *x;
        lasty = *y;
        *x = tx - quotient * *x;
        *y = ty - quotient * *y;
    }
    return b;
}

/* Modular multiplicative inverse of 1410000017 */
int inverse( int n );
int inverse( int n )
{
    int     x, y;

    egcd( n, 1410000017, &x, &y );
    return x;
}

/* Codility Kappa 2011 */
/* Modular arithmetic */
int solution( int T[], int D[], int N );
int solution( int T[], int D[], int N )
{
    int     factorial[ 1000001 ], result, i;

    for ( factorial[ 0 ] = i = 1; i <= 1000000; ++i ) {
        long long fac = (long long)i * factorial[ i - 1 ];
        fac %= 1410000017LL;
        factorial[ i ] = (int)fac;
    }
    for ( result = 1, i = 0; i < N; ++i ) {
        long long bino = factorial[ T[ i ] ];
        bino = (bino * inverse( factorial[ D[ i ] ] )) % 1410000017LL;
        bino = (bino * inverse( factorial[ T[ i ] - D[ i ] ] )) % 1410000017LL;
        bino = (result * bino) % 1410000017LL;
        if ( bino < 0 )
            bino += 1410000017LL;
        result = (int)bino;
    }
    return result;
}

int main( void )
{
    int T[] = { 6, 4, 7 }, D[] = { 1, 3, 4 };

    printf( "%d\n", solution( T, D, 3 ) );
    return 0;
}
