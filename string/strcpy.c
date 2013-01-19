#include <stdio.h>

/* Copy string from src to dest */
char *strcpy( char * restrict dest, const char * restrict src );
char *strcpy( char * restrict dest, const char * restrict src )
{
    for ( char *destP = dest; (*destP++ = *src++); )
        ;
    return dest;
}


int main( void )
{
    char    a[] = "Hello", b[6];

    printf( "%s\n", strcpy( b, a ) );
    return 0;
}

