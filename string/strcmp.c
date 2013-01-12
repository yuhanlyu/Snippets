#include <stdio.h>

/* Compare two strings */
int strcmp( const char s1[], const char s2[] );

int strcmp( const char s1[], const char s2[] )
{
    for (; *s1 && ( *s1 == *s2 ); ++s1, ++s2)
        ;
    // By standard, return value is determined by the sign of the 
    // difference between the values of the first pair of characters 
    // (both interpreted as unsigned char) that differ in the objects being compared.
    return *(const unsigned char *)s1 - *(const unsigned char *)s2;
}

int main( void )
{
    printf( "%d\n", strcmp( "aaa", "aab" ) );

    return 0;
}
