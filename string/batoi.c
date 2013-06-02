#include <stdio.h>

/* Convert binary string to integer */
unsigned batoi( const char s[] );
unsigned batoi( const char s[] )
{
    unsigned result = 0;

    while ( *s )
        result = ( result << 1 ) | ( (unsigned) *s++ - '0' );
    return result;
}

int main( void )
{
    printf( "%u\n", batoi( "111" ) );
    return 0;
}
