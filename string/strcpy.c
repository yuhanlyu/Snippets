#include <stdio.h>

/* Copy string from src to dest */
char *strcpy( char * restrict dest, const char * restrict src );
char *strcpy( char * restrict dest, const char * restrict src )
{
    char    *originDest = dest;
    while ( (*dest++ = *src++) )
        ;
    return originDest;
}


int main( void )
{
    char    a[] = "Hello", b[6];

    printf( "%s\n", strcpy( b, a ) );
    return 0;
}

