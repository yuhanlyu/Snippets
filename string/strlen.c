#include <stdio.h>

/* Compute the length of the string */
size_t strlen( const char string[] );
size_t strlen( const char string[] )
{
    for ( size_t len = 0; ; ++len )
        if ( !*string++ )
            return len;
}

int main( void )
{
    char    a[] = "Hello";

    printf( "%zd\n", strlen( a ) );
    return 0;
}

