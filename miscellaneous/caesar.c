#include <stdio.h>
#include <ctype.h>
#define OFFSET 3

int main( void )
{
    char    input[ 100 ];
    int     i;

    while ( gets( input ) != NULL ) {
        for ( i = 0; input[ i ] != '\0'; ++i )
            if ( isupper( input[ i ] ) )
                input[ i ] = ( input[ i ] - 'A' + OFFSET ) % 26 + 'A';
            else
                input[ i ] = ( input[ i ] - 'a' + OFFSET ) % 26 + 'a';
        puts( input );
    }
    return 0;
}

