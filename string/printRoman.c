#include <stdio.h>

void printRomanNumber( int decimal );

/* Print the roman numeral of decimal */
void printRomanNumber( int decimal )
{
    const int  s[] = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    const char *output[] = { "M", "CM", "D", "CD", "C", "XC", "L",
                             "XL", "X", "IX", "V", "IV", "I" };
    for ( int i = 0; decimal > 0; ++i ) {
        while ( decimal >= s[ i ] )  {
            printf( "%s", output[i] );
            decimal -= s[i];
        }
    }
}
                                                                                
int main( void )
{
    printf( "1910 should be MCMX: " );
    printRomanNumber( 1910 );
    puts( "" );
    printf( "1954 should be MCMLIV: " );
    printRomanNumber( 1954 );
    puts( "" );
    return 0;
}
