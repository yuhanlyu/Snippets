#include <stdio.h>
#include <math.h>

int main( void )
{
    double  a, b, c, d;

    while ( scanf( "%lf %lf %lf", &a, &b, &c ) == 3 ) {
        d = b * b - 4 * a * c;
        if ( d < 0.0 )
            puts( "No root" );
        else if ( d == 0.0 )
            printf( "Double roots: %f\n", -b / ( 2.0 * a ) );
        else
            printf( "Root 1 : %.2f Root 2 : %.2f\n", 
               (-b + sqrt( d )) / (2.0 * a), (-b - sqrt( d )) / (2.0 * a) );
    }
    return 0;
}

