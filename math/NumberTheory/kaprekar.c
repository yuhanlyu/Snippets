#include <stdio.h>
#define SWAP( A, B ) { tmp = A, A = B, B = tmp; }
#define MAX 4
#define MAGIC 6174

// Find Kaprekar number
int main( void )
{
    int     i, j, min, max;
    char    buf[ MAX + 1 ], tmp;

    while ( gets( buf ) != NULL ) {
        do {
            for ( i = 0; i < MAX; ++i )
                for ( j = MAX - 1; j > i; --j )
                    if ( buf[ j - 1 ] > buf[ j ] )
                        SWAP( buf[ j - 1 ], buf[ j ] );
            sscanf( buf, "%d", &min );
            for ( i = 0, j = MAX - 1; i < j; ++i, --j )
                SWAP( buf[ i ], buf[ j ] );
            sscanf( buf, "%d", &max );
            max -= min;
            sprintf( buf, "%d", max );
            puts( buf );
        } while ( max != MAGIC );
    }
    return 0;
}

