#include <stdio.h>

/* Compare b1 and b2 by n bytes */
int memcmp( const void *b1, const void *b2, size_t n );
int memcmp( const void *b1, const void *b2, size_t n )
{
    /* If n == 0, then must return 0 */
    if ( n == 0 ) return 0;
    const unsigned char *p1 = b1, *p2 = b2;
    for ( ; --n && *p1 == *p2; ++p1, ++p2 )
        ;
    return *p1 - *p2;
}

int main( void )
{
    char    a[] = "Hello", b[] = "Hell";

    printf( "%d\n", memcmp(a, b, 4) );
    return 0;
}

