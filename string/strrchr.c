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
    char    a[] = "Hello";

    printf( "%c\n", *strrchr( a, 'l' ) );
    return 0;
}

