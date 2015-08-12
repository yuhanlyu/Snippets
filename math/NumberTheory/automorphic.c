#include<stdio.h>

// Find automorphic number
int main( void )
{
    int     i;

    for ( i = 100; i < 1000; ++i )
        if ( ( i * i ) % 1000 == i )
            printf( "%d\n", i );
    return 0;
}

