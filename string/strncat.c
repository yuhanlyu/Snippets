#include <stdio.h>

char *strncat( char * restrict dest, const char * restrict src, size_t n );
char *strncat( char * restrict dest, const char * restrict src, size_t n )
{
    char    *originDest = dest;

    while ( *dest )
        ++dest;
    for ( ; n-- && (*dest = *src++); ++dest )
        ;
    *dest = '\0';
    return originDest;
}

int main( void )
{
    char    a[ 100 ] = "Test ", b[] = "Hello World";

    printf( "%s\n", strncat( a, b, 6 ) );
    return 0;
}
