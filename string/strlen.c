#include <stdio.h>

/* Compute the length of the string */
size_t strlen( const char *string );
size_t strlen( const char *string )
{
    size_t  len;

    for ( len = 0; *string++ != '\0'; ++len )
        ;
    return len;
}

int main( void )
{
    char    a[] = "Hello";

    printf( "%zd\n", strlen( a ) );
    return 0;
}

