#include <stdio.h>

/* String copy for n characters */
char *strncpy( char * restrict dest, char * restrict src, size_t n );
char *strncpy( char * restrict dest, char * restrict src, size_t n )
{
    char    *destP = dest;

    /* Copy at most n characters or until src is copied */
    do {
        if ( !n-- )
            return dest;
    } while ( (*destP++ = *src++) );

    /* Fill the remaining characters as null character */
    while( n-- )
        *destP++ = '\0';
    return dest;
}

int main( void )
{
    char    a[ 100 ], b[] = "Hello World";

    printf( "%s\n", strncpy( a, b, 6 ) );
    return 0;
}
