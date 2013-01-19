#include <stdio.h>

extern char *strchr( const char s1[], int c );

/* Find the longest prefix of s1 that are characters in s2 */
size_t strspn( const char s1[], const char s2[]);
size_t strspn( const char s1[], const char s2[])
{
    for ( size_t len = 0; ; ++len )
        if ( !*s1 || !strchr( s2, *s1++ ) )
            return len;
}

int main( void )
{
    char    a[] = "Hello", b[] = "eH";

    printf( "%zd\n", strspn( a, b ) );
    return 0;
}

