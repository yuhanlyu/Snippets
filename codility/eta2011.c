#include <stdio.h>

int solution( int A[], int N );
int solution( int A[], int N )
{
    int vertex_count[ 200001 ] = { 0 }, edge_count[ 200001 ][ 3 ], i, j;

    for ( i = 0; i < 200001; ++i )
        edge_count[i][0] = edge_count[i][1] = edge_count[i][2] = -200001;

    /* vertex_count stores the number of occurances of a vertex in the tour */
    /* We only consider an edge (s, t) in the form s < t */
    /* edge_count[i][j] = -200001, if there is at most j edges for vertex i */
    /* edge_count[i][j] = t, if the j-th edge for vertex i is t and occur once*/
    /* edge_count[i][j] = -t, if the j-th edge for vertex i is t and occur twice */
    for ( i = 0; i < N; ++i ) {
        int s = A[ i ], t = A[ ( i + 1 ) % N ];
        ++vertex_count[ A[ i ] ];
        if ( s == t )
            return -2;
        if ( s > t ) {
            int temp = s;
            s = t;
            t = temp;
        }
        for ( j = 0; j < 3; ++j ) {
            if ( edge_count[ s ][ j ] == -200001 ) {
                edge_count[ s ][ j ] = t;
                break;
            } else if ( edge_count[ s ][ j ] == t ) {
                edge_count[ s ][ j ] = -t;
                break;
            } else if ( edge_count[ s ][ j ] == -t ) {
                return -2;
            }
        }
    }
    for ( i = 0; i < N / 2 + 1; ++i ) {
        if ( vertex_count[ i ] != 1 && vertex_count[ i ] != 3 )
            return -2;
        for ( j = 0; j < 3; ++j ) {
            if ( edge_count[ i ][ j ] > 0 )
                return -2;
        }
    }
    /* By case analysis, the graph has only 3 hamilotian circuits */
    return 3;
}

int main( void )
{
    int A[] = { 4, 0, 4, 3, 4, 1, 5, 1, 7, 6, 7, 2, 7, 1 };
    int B[] = { 4, 4, 0, 3, 4, 1, 5, 1, 7, 6, 7, 2, 7, 1 };
    int C[] = { 3, 6, 3, 1, 5, 1, 0, 1, 3, 7, 3, 2, 3, 4 };
    int D[] = { 4, 0, 5, 0, 3, 0, 1, 3, 2, 3 };
    printf( "%d\n", solution( A, 14 ) );
    printf( "%d\n", solution( B, 14 ) );
    printf( "%d\n", solution( C, 14 ) );
    printf( "%d\n", solution( D, 10 ) );
    return 0;
}
