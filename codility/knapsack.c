#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Bounded Knapsack Problem */
int solution( int A[], int N );
int solution( int A[], int N )
{
    int     subsum[ 2 ][ 500000 ] = { { 0 } };
    int     item[ 102 ] = { 0 }, bound[ 102 ] = { 0 };
    int     sum, items, avg, current, i, j, k;

    /* Extreme case */
    if ( N == 0 )
        return 0;

    /* Calculate the types of items their numbers */
    for ( sum = i = 0; i < N; ++i ) {
        j = abs( A[ i ] );
        sum += j;
        ++bound[ j ];
    }
    avg = sum / 2;

    /* Remove all zero item */
    for ( items = 0, i = 1; i <= 100; ++i ) {
        while ( i <= 100 && bound[ i ] == 0 )
            ++i;
        if ( i <= 100 ) {
            item[ items ] = i;
            bound[ items++ ] = bound[ i ];
        }
    }

    /* Inductive case:
     * Subsum(i, j) is the maxium sum not exceeding j using the first i items
     * Used( i, j ) is the number of i-th item used in the solution
     * Subsum(i, j) = max( subsum(i-1, j), subsum(i, j-1), 
     *                     subsum(i, j - item[ i ]) )
     * Since DP only depends on the previous level, we can reduce the space */
    for ( current = i = 0; i < items; ++i, current = !current ) {
        int used[ 500000 ] = { 0 };
        for ( j = 1; j <= avg; ++j ) {
            subsum[ current ][ j ] = subsum[ !current ][ j ];
            if ( subsum[ current ][ j - 1 ] > subsum[ current ][ j ] ) {
                subsum[ current ][ j ] = subsum[ current ][ j - 1];
                used[ j ] = used[ j - 1 ];
            }
            k = j - item[ i ];
            if ( k >= 0 && used[ k ] < bound[ i ] &&
              subsum[ current ][ k ] + item[ i ] > subsum[ current ][ j ] ) {
                subsum[ current ][ j ] = subsum[ current ][ k ] + item[ i ];
                used[ j ] = used[ k ] + 1;
            }
        }
    }
    return sum - 2 * subsum[ !current ][ avg ];
}

int main(void)
{
    int A[] = { 1, 2, 3, 5};
    printf( "%d\n", solution( A, 4 ) );
    return 0;
}
