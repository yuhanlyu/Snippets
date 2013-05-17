#include <stdio.h>

char *itoa( int n, char s[], int base );
char *strrev( char s[] );

/* Convert integer to string */
char *itoa( int n, char s[], int base )
{
    char    *p = s;
    int     isNegative = n < 0;

    if ( isNegative ) {
        *p++ = '-';
        n = -n;
    }
    /* Generate characters one by one from LSD to MSD, this also works when n = 0 */
    do {
        int digit = n % base;
        *p++ = digit <= 9 ? digit + '0' : digit + 'a' - 10;
    } while ( ( n /= base ) != 0 );
    *p++ = '\0';
    /* Reverse the string to get order from MSD to LSD */
    strrev( s + isNegative );
    return s;
}

char *strrev( char s[] )
{
    char    *right;

    if ( s == NULL || *s == '\0' )
        return s;
    for ( right = s; right[ 1 ] != '\0'; ++right )
        ;
    for ( char *left = s; left < right; ++left, --right ) {
        char temp = *left;
        *left = *right;
        *right = temp;
    }
    return s;
}

int main( void )
{
    char    buf[ 1000 ];

    printf( "%s\n", itoa( 1234567, buf, 10 ) );
    printf( "%s\n", itoa( -1234567, buf, 10 ) );
    printf( "%s\n", itoa( 0, buf, 10 ) );
    printf( "%s\n", itoa( -0, buf, 10 ) );
    printf( "%s\n", itoa( 255, buf, 16 ) );
    printf( "%s\n", itoa( 255, buf, 2 ) );
    return 0;
}
