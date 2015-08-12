#include <stdio.h>

int main( void )
{
    double  ans = 0.0;
    int     i, n;

    scanf( "%d". &n );
    for ( i = 1; i < n; ++i )
        ans += 1.0 / i;
    printf( "%f\n", ans );
    return 0;
}

