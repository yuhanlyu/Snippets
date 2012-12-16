#include <stdio.h>
#define NUM_OF_ROMAN_LETTERS 7

/* Converting a roman numerals to an integer */
int romanToDecimal( const char *roman );
int romanToDecimal( const char *roman )
{
    static int     numeralMap[] = { 1, 5, 10, 50, 100, 500, 1000 };
    static char    romanMap[] = { 'I', 'V', 'X', 'L', 'C', 'D', 'M' };
    int            decimal = 0, indexOfRoman, indexOfMap, lastIndexOfMap = -1;

    for ( indexOfRoman = 0; roman[ indexOfRoman ] != '\0'; ++indexOfRoman ) {
        /* Find the value of the current numeral */
        for ( indexOfMap = 0; indexOfMap < NUM_OF_ROMAN_LETTERS; ++indexOfMap )
            if ( romanMap[ indexOfMap ] == roman[ indexOfRoman ] )
                break;
        /* If the value found last time is smaller than the current value,
         * then subtract twice of the last value */
        if ( lastIndexOfMap >= 0 && lastIndexOfMap < indexOfMap )
            decimal -= numeralMap[ lastIndexOfMap ] * 2;
        decimal += numeralMap[ indexOfMap ];
        lastIndexOfMap = indexOfMap;
    }
    return decimal;
}
                                                                                
int main( void )
{
    printf( "Decimal of MDCCCCX should be 1910: %d\n", 
                                     romanToDecimal( "MDCCCCX" ) );

    printf( "Decimal of MCMXC should be 1990: %d\n", 
                                     romanToDecimal( "MCMXC" ) );
    return 0;
}
