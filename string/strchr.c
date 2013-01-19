#include <stdio.h>

/* Locate the first occurence of c in string */
char *strchr( const char string[], int c);
char *strchr( const char string[], int c)
{
    /* Since c can be '\0', thus we cannot test *string first */
    while ( *string != (char)c )
        if (!*string++)
            return NULL;
    return (char *)string;
}

int main( void )
{
    printf( "strchr( \"\", '\\0' ) should be an empty string: %s\n", 
             strchr( "", '\0' ) );
    printf( "strchr( \"Hello\", '\\0' ) should be an empty string: %s\n", 
             strchr( "", '\0' ) );
    printf( "strchr( \"Hello\", 'H' ) should be Hello: %s\n", 
             strchr( "Hello", 'H' ) );
    printf( "strchr( \"Hello\", 'e' ) should be ello: %s\n", 
             strchr( "Hello", 'e' ) );
    printf( "strchr( \"Hello\", 'x' ) should be null: %p\n", 
             strchr( "Hello", 'x' ) );
    return 0;
}

