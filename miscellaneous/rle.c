#include <stdio.h>
#define MAX 255

void RLE( char buf[] );

int main( void )
{
    char    buf[ MAX ];

    while ( gets( buf ) != NULL )
        RLE( buf );
    return 0;
}

void RLE( char buf[] )
{
    int     i, count;
    char    previous;

    for ( i = 0; buf[ i ] != '\0'; ++i ) {
        putchar( buf[ i ] );
        previous = buf[ i ];
        for ( count = 1, ++i; buf[ i ] != '\0'; ++i )
            if ( buf[ i ] == previous )
                count++;
            else {
                printf( "%d", count );
                --i;
                break;
            }
        if ( buf[ i ] == '\0' ) {
            printf( "%d\n", count );
            break;
        }
    }
}

