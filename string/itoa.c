#include <stdio.h>

char *itoa( int n, char s[] );
char *strrev( char s[] );

char *itoa( int n, char s[] )
{
    char    *p = s;
    int     isNegative = n < 0;

    if ( isNegative ) {
        *p++ = '-';
        n = -n;
    }
    do {
        *p++ = n % 10 + '0';
    } while ( ( n /= 10 ) != 0 );
    *p++ = '\0';
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

    printf( "%s\n", itoa( 1234567, buf ) );
    printf( "%s\n", itoa( -1234567, buf ) );
    printf( "%s\n", itoa( 0, buf ) );
    printf( "%s\n", itoa( -0, buf ) );
    return 0;
}
