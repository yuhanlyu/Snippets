#include <stdio.h>

extern char *strchr( const char s1[], int c );

/* String pointer break: 
 * search the first occurence in s1 that is a character in s2
 */
char *strpbrk( const char s1[], const char s2[] );
char *strpbrk( const char s1[], const char s2[] )
{
    while ( *s1 )
        if ( strchr( s2, *s1++ ) )
            return (char *)s1 - 1;
    return NULL;
}

int main( void )
{
    char    a[] = "Hello", b[] = "elo";

    printf( "%s\n", strpbrk( a, b ) );
    return 0;
}

