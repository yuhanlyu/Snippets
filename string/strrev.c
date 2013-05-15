#include <stdio.h>

/* Reverse a string */
char *strrev( char s[] );
char *strrev( char s[] )
{
    char    *right;

    if ( s == NULL || *s == '\0' )
        return s;
    for ( right = s; right[ 1 ] != '\0'; ++right )
        ;
    for ( char *left = s; left < right; ++left, --right ) {
        char temp = *left;
        *left = *right;
        *right = temp;
    }
    return s;
}

int main( void )
{
    char    buf[] = "Hello World";
    puts( strrev( buf ) );
    return 0;
}
