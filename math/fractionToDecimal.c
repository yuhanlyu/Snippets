#include <stdio.h>

int main( void )
{
    int     denominator, numerator, i, j, temp, two, five;

    scanf( "%d %d", &numerator, &denominator );
    printf( "%d", numerator / denominator );
    numerator %= denominator;
    if ( numerator != 0 ) {
        putchar( '.' );
        i = numerator;
        j = denominator;
        while ( ( i %= j ) && ( j %= i ) )
            ;
        numerator /= i + j;
        denominator /= i + j;
        for ( temp = denominator, two = 0; temp % 2 == 0; ++two )
            temp /= 2;
        for ( temp = denominator, five = 0; temp % 5 == 0; ++five )
            temp /= 5;
        for ( i = 0; i < two || i < five; ++i ) {
            numerator *= 10;
            printf( "%d", numerator / denominator );
            numerator %= denominator;
        }
        if ( numerator != 0 ) {
            putchar( '(' );
            temp = numerator;
            do {
                numerator *= 10;
                printf( "%d", numerator / denominator );
                numerator %= denominator;
            } while ( temp != numerator );
            putchar( ')' );
        }
    }
    puts( "" );
    return 0;
}

