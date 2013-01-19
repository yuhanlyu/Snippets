#include <stdio.h>

/* Memory copy for n bytes */
void *memcpy(void *restrict dest, const void *restrict src, size_t n);
void *memcpy(void *restrict dest, const void *restrict src, size_t n)
{
    char *destP = dest;
    for ( const char *srcP = src; n--; )
        *destP++ = *srcP++;
    return dest;
}


int main( void )
{
    char    a[] = "Hello", b[] = "World";

    printf( "%s\n", (char *)memcpy( a, b, 5 ) );
    return 0;
}

