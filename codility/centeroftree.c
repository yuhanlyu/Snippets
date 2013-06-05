#include <stdio.h>

int solution( int T[], int N );
int solution( int T[], int N )
{
    long long pathlength[ 100000 ]; /* Avoid overflow */
    int     degree[ 100000 ] = { 0 }, order[ 100000 ], subtreesize[ 100000 ];
    int     tail, i;

    /* Compute degree */
    for ( i = 0; i < N; ++i ) {
        if ( T[ i ] != i )
            ++degree[ T[ i ] ];
    }

    /* Compute reverse level order (kind of) */
    for ( i = tail = 0; i < N; ++i ) {
        if ( degree[ i ] == 0 )
            order[ tail++ ] = i;
    }
    for ( i = 0; i < N - 1; ++i ) {
        int child = order[ i ];
        if ( --degree[ T[ child ] ] == 0 )
            order[ tail++ ] = T[ child ];
    }

    for ( i = 0; i < N; ++i )
        subtreesize[ i ] = 1;
    /* Calculate the subtree size for each node */
    /* Calculate the path length go down the tree */
    /* Path length of parent to child = path length of child 
     *                                + size of subtree */
    for ( i = 0; i < N - 1; ++i ) {
        int child = order[ i ];
        subtreesize[ T[ child ] ] += subtreesize[ child ];
        pathlength[ T[ child ] ] += pathlength[ child ] + subtreesize[ child ];
    }

    /* Calculate the path length */
    /* Now, root has correct pathlength */
    /* Path length of child = pathlength of parent - subtreesize of child
     *                        + N - subtreesize of child */
    for ( i = N - 2; i >= 0; --i ) {
        int child = order[ i ], parent = T[ child ];
        pathlength[ child ] = pathlength[ parent ] - 2*subtreesize[ child ] + N;
    }

    /* Find the minimum */
    for ( tail = 0, i = 1; i < N; ++i ) {
        if ( pathlength[ i ] < pathlength[ tail ] )
            tail = i;
    }
    return tail;
}

int main( void )
{
    int     T[] = { 9, 1, 4, 9, 0, 4, 8, 9, 0, 1 };

    printf( "%d\n", solution( T, 10 ) );
    return 0;
}
