#include <stdio.h>
#define ABS(a) ( (a) > 0 ? (a) : -(a) )

int main( void )
{
    int     i;

    for ( i = -4; i <= 4; ++i )
        puts( "*****" + 4 - ABS( i ) );
    return 0;
}

