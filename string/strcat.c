#include <stdio.h>

/* Concate the string src to the end of string dest */
char *strcat( char *dest, const char *src );

char *strcat( char *dest, const char *src )
{
    char    *destP = dest;

    /* Move to the end of dest */
    while ( *destP )
        ++destP;
    /* Copy src to the end of dest */
    while ( (*destP++ = *src++) )
        ;
    return dest;
}

int main( void )
{
    char    a[15] = "Hello ", b[] = "World";

    puts( strcat(a, b) );
    return 0;
}
