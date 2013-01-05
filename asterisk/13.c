#include <stdio.h>
#define ABS(a) ( (a) > 0 ? (a) : -(a) )

int main( void )
{
    int     i;

    for ( i = -4; i <= 4; ++i )
        printf( "%*s*%s\n", ABS( i ), "", ABS( i ) == 4 ? "" :
                "       *" + ABS( i ) * 2 );
    return 0;
}

