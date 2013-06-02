#include <stdio.h>

/* Dynamic Pogramming */
int solution ( int **A, int N, int M, int K );
int solution ( int **A, int N, int M, int K )
{
    int     dp[ 1000 ] = { K }, i, j, right;

    for ( i = 0; i < N; ++i ) {
        for ( right = j = 0; j < M; right = K - dp[ j ], j++ ) {
            K = right + dp[ j ];
            if ( A[ i ][ j ] == 1 )
                dp[ j ] = K / 2;
            else if ( A[ i ][ j ] == -1 )
                dp[ j ] = K / 2 + K % 2;
        }
    }
    return dp[ M - 1 ];
}

int main( void )
{
    int     AA[ 2 ][ 3 ] = { {-1, 0, 1}, {1, 0, 0} };
    int     *A[ 2 ] = { AA[ 0 ], AA[ 1 ] };

    printf( "%d\n", solution(A, 2, 3, 4) );
    return 0;
}
