#include <stdio.h>

extern char *strchr( const char s1[], int c );

/* Find the longest prefix of s1 that are characters not in s2 */
size_t strcspn( const char s1[], const char s2[]);
size_t strcspn( const char s1[], const char s2[])
{
    size_t len = 0;

    while ( *s1 && !strchr( s2, *s1++ ) )
        ++len;
    return len;
}

int main( void )
{
    char    a[] = "Hello", b[] = "lo";

    printf( "%zd\n", strcspn( a, b ) );
    return 0;
}

