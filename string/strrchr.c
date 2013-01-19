#include <stdio.h>

/* Locate the last occurence of c in string */
char *strrchr( const char string[], int c);
char *strrchr( const char string[], int c)
{
    char *occur = NULL;

    /* c can be '\0', thus we should compare first */
    do {
        if ( *string == (char)c )
            occur = (char *)string;
    } while ( *string++ );
    return occur;
}

int main( void )
{
    printf( "strrchr( \"\", '\\0' ) should be an empty string: %s\n",
             strrchr( "", '\0' ) );
    printf( "strrchr( \"Hello\", '\\0' ) should be an empty string: %s\n",
             strrchr( "Hello", '\0' ) );
    printf( "strrchr( \"Hello\", 'o' ) should be o: %s\n",
             strrchr( "Hello", 'o' ) );
    printf( "strrchr( \"Hello\", 'H' ) should be Hello: %s\n",
             strrchr( "Hello", 'H' ) );
    printf( "strrchr( \"Hello\", 'l' ) should be lo: %s\n",
             strrchr( "Hello", 'l' ) );
    return 0;
}

