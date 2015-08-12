#include <stdio.h>
#define MAX 19

int main( void )
{
    int     ramsey[ MAX ][ MAX ];
    int     i, j;

    for ( i = 2; i < MAX; ++i )
        ramsey[ i ][ 2 ] = ramsey[ 2 ][ i ] = i;
    for ( i = 3; i < MAX; ++i )
        for ( j = 3; j < MAX; ++j )
            if ( ( ramsey[i - 1][j] % 2 == 1 )
                    || ( ramsey[i][j - 1] % 2 == 1 ) )
                ramsey[i][j] = ramsey[i - 1][j] + ramsey[i][j - 1];
            else
                ramsey[ i ][ j ] = ramsey[i - 1][j] + ramsey[i][j - 1] - 1;

    while ( scanf( "%d %d", &i, &j ) == 2 )
        printf( "%d\n", ramsey[ i ][ j ] );
    return 0;
}

