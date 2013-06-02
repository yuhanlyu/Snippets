#include <stdio.h>

int solution ( int D[], int P[], int N, int T );
int solution ( int D[], int P[], int N, int T )
{
    int     farthest[ 100000 ], lower[ 100000 ];
    int     result, remain, refill, far, next_low, next, need, i, j;

    /* farthest[ i ] = j, if j is the farthest gas station that i can reach with a full tank */
    for ( remain = T, i = far = 0; i < N; ++i ) {
        while ( far < N && remain >= D[ far ] ) {
            remain -= D[ far ];
            ++far;
        }
        if ( far == i )
            return -1;
        else {
            farthest[ i ] = far;
            remain += D[ i ];
        }
    }

    /* lower[ i ] = j, if j > i, P[ j ] < P[ i ] and P[ k ] > P[ i ] for all i < k < j */
    for ( lower[ N - 1 ] = N, i = N - 2; i >= 0; --i ) {
        if ( P[ i + 1 ] < P[ i ] ) {
            lower[ i ] = i + 1;
        } else {
            for ( next_low = lower[ i + 1 ]; next_low != N && P[ next_low ] >= P[ i ]; )
                next_low = lower[ next_low ];
            lower[ i ] = next_low;
        }
    }

    for ( result = remain = i = 0; i < N; i = next ) {
        /* Cannot find a lower price, just fill full tank and move to i + 1*/
        if ( lower[ i ] > farthest[ i ] ) {
            refill = T - remain;
            remain = T - D[ i ];
            next = i + 1;
        } else {
            /* Move to lower[ i ] */
            for ( need = 0, j = i; j < lower[ i ]; ++j )
                need += D[ j ];
            refill = ( remain < need ? need - remain : 0 );
            remain += refill - need;
            next = lower[ i ];
        }

        if ( result + (unsigned long long)P[ i ] * refill  > 1000000000 )
            return -2;
        else
            result += P[ i ] * refill;
    }
    return result;
}

int main( void )
{
    int D[] = { 10, 9, 8 }, P[] = { 2, 1, 3 };

    printf( "%d\n", solution( D, P, 3, 15 ) );
    return 0;
}
