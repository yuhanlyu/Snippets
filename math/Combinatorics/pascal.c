#include <stdio.h>

int main( void )
{
    int     n, i, j;

    while( scanf("%d", &n) == 1 && n > 0 ) {
        int     table[50] = {0, 1};

        printf( "%3d\n", 1 );
        for( i = 1; i < n; ++i, puts( "" ) ) {
            for( j = i + 1; j > 0; --j )
                table[j] = table[j - 1] + table[j];
            for( j = 1; j < i + 2; ++j )
                printf( "%3d", table[j] );
        }
    }
    return 0;
}

