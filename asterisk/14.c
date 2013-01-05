#include <stdio.h>
#define ABS(a) ( (a) > 0 ? (a) : -(a) )

int main( void )
{
    int     i;

    for ( i = -4; i <= 4; ++i )
        printf( "%*s*%s\n", 4 - ABS( i ), "", i == 0 ? "" :
                "       *" + 8 - ABS( i ) * 2 );
    return 0;
}

