#include <stdio.h>

double eval( double p[], double x, int n );

int main( void )
{
    double p[] = { 3, 5, 1 };  /* 3x^2 + 5x + 1 */

    printf( "%f\n", eval( p, 2.0, 2 ) );
    return 0;
}

double eval( double p[], double x, int n )
{
    int     i;
    double  ans = p[ 0 ];

    for ( i = 1; i <= n; ++i )
        ans = ans * x + p[ i ];
    return ans;
}

