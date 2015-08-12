#include <stdio.h>

int main( void )
{
    int  a, b, t;

    while ( scanf( "%d %d", &a, &b ) == 2 )
    {
        printf( "[%d;", a / b );
        do {
            t = a % b;
            a = b;
            b = t;
        } while ( b != 1 && printf( "%d,", a / b ) );
        printf( "%d]\n", a );
    }
    return 0;
}

