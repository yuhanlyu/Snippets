#include <stdio.h>

int main( void )
{
    int     i;

    for ( i = 4; i >= 0; --i )
        puts( "*****" + i );
    return 0;
}

