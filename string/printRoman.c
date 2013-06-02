#include <stdio.h>

void printRomanNumber( int decimal );

/* Print the roman numeral of decimal */
void printRomanNumber( int decimal )
{
    static const int  s[]       = {  1000,  900,  500,  400,  100,   90,  50, 
                                       40,   10,    9,    5,    4,    1 };
    static const char *output[] = {   "M", "CM",  "D", "CD",  "C", "XC", "L",
                                     "XL",  "X", "IX",  "V", "IV",  "I" };

    /* Start from the largest roman numeral */
    for ( int index = 0; decimal > 0; ++index ) {
        /* Output the roman numeral add subtract the corresponding value */
        while ( decimal >= s[ index ] )  {
            printf( "%s", output[ index ] );
            decimal -= s[ index ];
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
