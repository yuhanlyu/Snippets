#include <stdio.h>

/* Set memory content to c */
void *memset ( void *block, int value, size_t n );
void *memset ( void *block, int value, size_t n )
{
    unsigned char *p = block;

    while ( n-- ) 
        *p++ = (unsigned char)value;
    return block;
}


int main( void )
{
    char    a[] = "Hello";

    printf( "%s\n", (char *)memset( a, 'a', 5 ) );
    return 0;
}

