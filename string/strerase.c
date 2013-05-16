#include <stdio.h>

/* Erase the character from s1, if the character is in s2 */
char *strerase( char s1[], const char s2[]);
char *strerase( char s1[], const char s2[])
{
    int     current;

    for ( int j, i = current = 0; s1[ i ] != '\0'; ++i ) {
        for ( j = 0; s2[ j ] != '\0' && s2[ j ] != s1[ i ]; ++j )
            ;
        if ( s2[ j ] == '\0' )
            s1[ current++ ] = s1[ i ];
    }
    s1[ current ] = '\0';
    return s1;
}

int main( void )
{
    char    buf[] = "Hello World";
    puts( strerase( buf, "Hello" ) );
    return 0;
}


