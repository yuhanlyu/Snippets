#include <stdio.h>
#include <ctype.h>
#define ALPHA 26
#define DIGIT 10
#define MAX 20

/* Print the morse code for the character c */
void printMorse(char c);
void printMorse(char c)
{
    const char *alpha[ ALPHA ] = { ".-", "-...", "-.-.", "-..", ".", "..-.",
           "--.", "....", "..", ".---", "-.-", ".-..",
        "--", "-.", "---", ".--.", "--.-", ".-.",
        "...", "-", "..-", "...-", ".--", "-..-",
        "-.--", "--.." };
    const char *digit[ DIGIT ] = { "-----", ".----", "..---", "...--", "....-",
        ".....", "-....", "--...", "---..", "----."};
    if ( c == ' ' )
        printf( "\\ " );
    else if ( isalpha( c ) )
        printf( "%s ", alpha[ toupper( c ) - 'A' ] );
    else if ( isdigit( c ) )
        printf( "%s ", digit[ c - '0' ] );
}

int main( void )
{
    char    buf[ MAX ];

    while ( gets( buf ) != NULL ) {
        for ( int i = 0; buf[ i ] != '\0'; ++i )
            printMorse( buf[ i ] );
        puts( "" );
    }
    return 0;
}
