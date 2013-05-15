#include <stdio.h>
#include <ctype.h>

/* Convert hex string to integer */
int htoi( const char str[] );
int htoi( const char str[] )
{
    if ( *str == '0' ) {
        ++str;
        if ( *str == 'x' || *str == 'X' )
            ++str;
    }

    int    n = 0;
    for ( ; isxdigit( *str ); ++str ) {
        if ( *str >= '0' && *str <= '9' )
            n = 16 * n + *str - '0';
        else if ( *str >= 'a' && *str <= 'f' )
            n = 16 * n + *str - 'a' + 10;
        else if ( *str >= 'A' && *str <= 'F' )
            n = 16 * n + *str - 'A' + 10;
    }
    return n;
}

int main( void )
{
    printf( "%d\n", htoi( "0xff" ) );
    return 0;
}
