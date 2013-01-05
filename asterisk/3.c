#include <stdio.h>

int main( void )
{
    int     i;

    for ( i = 0; i < 5; ++i )
        printf( "%5s\n", "*****" + i );
    return 0;
}

