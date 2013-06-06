#include <stdio.h>

/* Factorial */
int factorial( int n );
int factorial( int n )
{
    int     fac;

    for ( fac = 1; n > 1; --n )
        fac *= n;
    return fac;
}

int main( void )
{
    printf( "%d\n", factorial( 5 ) );
    return 0;
}
