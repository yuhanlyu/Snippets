#include <stdio.h>

/* Locate the first occurence of c in block */
void *memchr( const void *block, int c, size_t n );
void *memchr( const void *block, int c, size_t n )
{
    for ( const unsigned char *p = block; n--; ++p )
        if ( *p == (unsigned char)c )
            return (void *)p;
    return NULL;
}

int main( void )
{
    char    a[] = "Hello";

    printf( "%c\n", *(char *)memchr( a, 'l', 5 ) );
    return 0;
}

