#include <stdio.h>

/* String copy for n characters */
char *strncpy( char * restrict dest, char * restrict src, size_t n );
char *strncpy( char * restrict dest, char * restrict src, size_t n )
{
    char    *originDest = dest;

    /* Copy at most n characters or until src is copied */
    do {
        if ( !n-- )
            return originDest;
    } while ( (*dest++ = *src++) );

    /* Fill the remaining characters as null character */
    while( n-- )
        *dest++ = '\0';
    return originDest;
}

int main( void )
{
    char    a[ 100 ], b[] = "Hello World";

    printf( "%s\n", strncpy( a, b, 6 ) );
    return 0;
}
