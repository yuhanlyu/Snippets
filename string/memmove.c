#include <stdio.h>

extern void *memcpy(void *restrict s1, const void *restrict s2, size_t n);
/* Memory move for n bytes, dest and src may overlap */
void *memmove(void *dest, const void *src, size_t n);
void *memmove(void *dest, const void *src, size_t n)
{
    unsigned char temp[ n ];
    memcpy( temp, src, n );
    memcpy( dest, temp, n );
    return dest;

    /* By standard, comparison between pointers point to 
     * different array objects is undefined behavior.
     * Thus, there is no protable way to test
     * dest overlaps with src. 
     * In this implementation, it may fail if n is too large,
     * which will not happen by standard */

    /* Suppose that pointer comparison is allowed, 
     * we can do the following way */
    /*
    char *destP = dest;
    const char *srcP = src;
    // Safe to copy backward
    if ( srcP < destP && srcP + n > destP ) {
        for ( destP += n, srcP += n; n--; )
            *--destP = *--srcP;
    // Safe to copy forward
    } else if ( destP != srcP ) {
        while ( n-- )
            *destP++ = *srcP++;
    }
    return dest;
    */
}


int main( void )
{
    char    a[] = "Hello";

    printf( "%s\n", (char *)memmove( a, a + 2, 3 ) );
    return 0;
}

