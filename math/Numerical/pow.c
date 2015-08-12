#include <stdio.h>

double power( double x, int n );

int main( void )
{
    printf( "%f\n", power( 3.5, 7 ) );
    return 0;
}

double power( double x, int n )
{
    double  ans = 1.0;

    while ( n-- > 0 )
        ans *= x;
    return ans;
}

