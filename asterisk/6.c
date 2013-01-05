#include <stdio.h>

int main( void )
{
    int     i;

    for ( i = 4; i >= 0; --i )
        printf( "%*s\n", 5 + i, "*********" + 8 - i * 2 );
    return 0;
}

