#include <stdio.h>

void move( int n, char a, char b, char c );
int cnt;

int main( void )
{
    int     n;

    scanf( "%d", &n );
    move( n, 'A', 'B', 'C' );
    return 0;
}

void move( int n, char a, char b, char c )
{
    if ( n == 1 )
        printf( "%d Move disk 1 from tower %c to tower %c\n", ++cnt, a, c );
    else {
        move( n - 1, a, c, b );
        ++cnt;
        printf( "%d Move disk %d from tower %c to tower %c\n", cnt, n, a, c );
        move( n - 1, b, a, c );
    }
}

