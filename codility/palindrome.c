#include <stdio.h>
#include <string.h>

/* Manacher's algorithm */
int solution(char *s);
int solution(char *s)
{
    char    buf[40002];
    int     p[ 40002 ] = { 1 }, len = strlen(s), r = 0, c = 0, i;

    for ( i = 0; i < len; ++i ) {
        buf[ 2 * i ] = 'A';
        buf[ 2 * i + 1 ] = s[ i ];
    }
    buf[ len * 2 ] = 'A';
    buf[ len * 2 + 1 ] = '\0';

    /* c is the center of the longest palindromic substring(LPS) */
    /* r is the right boundary of this longest palindromic substring */
    for ( i = 1; buf[ i ] != '\0'; ++i ) {
        int mirror = 2 * c - i; /* mirror point of i w.r.t center c */
        /* If LPS does not cover i, brute force search */
        if ( r < i )
            p[ i ] = 1;
        /* If LPS cover i and the LPS centered at i exceeds the boundary,
         * then brute force search */
        else if ( p[ mirror ] >= r - i )
            p[ i ] = r - i;
        /* If LPS cover i and the LPS centered at i does not exceed 
         * the boundary, then p[ i ] = p[ mirror ].
         * In this case, buf[ i + p[ i ] ] != buf[ i - p[ i ] ] */
        else
            p[ i ] = p[ mirror ];
        /* Brute force search */
        while ( i - p[ i ] >= 0 && buf[ i + p[ i ] ] == buf[ i - p[ i ] ]) 
            ++p[ i ];
        /* Update center and boundar */
        if ( i + p[ i ] > r ) {
            r = i + p[ i ];
            c = i;
        }
    }
    for ( i = c = 0; buf[ i ] != '\0'; ++i )
        c += ( p[ i ] - 1 ) / 2;
    return c <= 100000000 ? c : -1;
}

int main(void)
{
    char s[] = "a";
    printf( "%d\n", solution( s ) );
}
