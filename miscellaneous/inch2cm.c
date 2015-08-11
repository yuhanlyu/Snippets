#include <stdio.h>

int main( void )
{
    double  n;

    while ( scanf( "%lf", &n ) == 1 )
        printf( "%.2f\n", 2.54 * n );
    return 0;
}

