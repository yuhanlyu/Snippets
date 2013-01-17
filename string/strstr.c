#include <stdio.h>

/* Find string s2 in string s1 */
char *strstr( const char s1[], const char s2[] );
char *strstr( const char s1[], const char s2[] )
{
    /* If s2 is an empty string, then should return s1 */
    if ( !*s2 ) return (char *)s1;
    const char *end = s1, *p2 = s2;
    for ( ; *++p2; ++end )
        /* If s1 is shorter than s2, then return NULL */
        if ( !*end )
            return NULL;
    /* begin to end is a string with length strlen(s2) */
    for ( const char *begin = s1; *end; ++end, ++begin ) {
        /* strncmp(begin, s2, end - begin + 1) */
        p2 = s2;
        for ( const char *p1 = begin; *p1 == *p2; ++p1, ++p2 )
            ;
        if ( !*p2 ) return (char *)begin;
    }
    return NULL;
}

int main( void )
{
    printf( "strstr( \"Hello\", \"el\" ) should be ello: %s\n", strstr( "Hello", "el" ) );
    printf( "strstr( \"Hello\", \"lo\" ) should be lo: %s\n", strstr( "Hello", "lo" ) );
    printf( "strstr( \"Hello\", \"xo\" ) should be NULL: %p\n", strstr( "Hello", "xo" ) );
    printf( "strstr( \"Hello\", \"Hello\" ) should be Hello: %s\n", strstr( "Hello", "Hello" ) );
    printf( "strstr( \"Hello\", \"\" ) should be Hello: %s\n", strstr( "Hello", "" ) );
    printf( "strstr( \"\", \"\" ) should be an empty string: %s\n", strstr( "", "" ) );
    printf( "strstr( \"\", \"Hello\" ) should be NULL: %p\n", strstr( "", "Hello" ) );

    return 0;
}
