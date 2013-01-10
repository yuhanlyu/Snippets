#include <stdio.h>

/* Concate the string src to the end of string dest */
char *strcat( char *dest, const char *src );

char *strcat( char *dest, const char *src )
{
    char    *originDest = dest;

    /* Move to the end of dest */
    while ( *dest )
        ++dest;
    /* Copy src to the end of dest */
    while ( (*dest++ = *src++) )
        ;
    return originDest;
}

int main( void )
{
    char    a[15] = "Hello ", b[] = "World";

    puts( strcat(a, b) );
    return 0;
}
