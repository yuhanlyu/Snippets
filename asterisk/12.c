#include <stdio.h>

int main( void )
{
    int     i;

    for ( i = 0; i < 10; ++i )
        puts( "* * * * *" + i % 2 );
    return 0;
}

