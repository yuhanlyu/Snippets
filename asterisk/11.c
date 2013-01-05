#include <stdio.h>
#define ABS(a) ( (a) > 0 ? (a) : -(a) )

int main( void )
{
    int     i;

    for ( i = -4; i <= 4; ++i )
        printf( "%5s\n", "*****" + ABS( i ) );
    return 0;
}

