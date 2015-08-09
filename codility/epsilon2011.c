#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int     a, b;
} Line;

double  solution( int A[], int B[], int N );
int     cmp( const void *a, const void *b );
double  evaluate( Line l, double x );
int     getEnvelope( Line lines[], int mode, int N, double points[][2], int index[] ); 
void    intersect( Line l1, Line l2, double point[] );

double solution( int A[], int B[], int N )
{
    Line    lines[ 100000 ];
    int     uindex[ 100000 ], lindex[ 100000 ], un, ln, i, j;
    double  upper[ 100000 ][ 2 ], lower[ 100000 ][ 2 ], result, distance;

    /* Initial and sort lines */
    for ( i = 0; i < N; ++i ) {
        lines[ i ].a = A[ i ];
        lines[ i ].b = B[ i ];
    }
    qsort( lines, N, sizeof( Line ), cmp );

    /* Calculate the envelope */
    un = getEnvelope(lines, 0, N, upper, uindex); 
    ln = getEnvelope(lines, 1, N, lower, lindex);

    /* Find the minimum */
    for ( result = 10000000.0, i = j = 1; i < un; ) {
        if ( upper[ i ][ 0 ] < lower[ j ][ 0 ] || j == ln - 1 ) {
            distance = upper[ i ][ 1 ] - 
                       evaluate( lines[ lindex[ j - 1 ] ], upper[ i ][ 0 ] );
            ++i;
        } else {
            distance = evaluate( lines[ uindex[ i - 1 ] ], lower[ j ][ 0 ] )
                       - lower[ j ][ 1 ];
            ++j;
        }
        if ( distance < result )
            result = distance;
    }
    return result;
}

/* For N lines with order by increasing slope, 
 * find the upper envelope if mode = 0,
 * find the lower envelope if mode = 1,
 * store the points in points array and indices in index array
 * return the number of points in the envelope */
int getEnvelope( Line lines[], int mode, int N, double points[][2], int index[] )
{
    int     begin = 0, end = N, step = 1, number, previous, i;

    if ( mode == 1 ) {
        begin = N - 1;
        end = -1;
        step = -1;
    }

    points[ 0 ][ 0 ] = -10000000.0;
    points[ 0 ][ 1 ] = evaluate( lines[ begin ], points[ 0 ][ 0 ] );
    previous = index[ 0 ] = begin;

    for ( number = 1, i = begin + step; i != end; i += step ) {
        if( lines[ i ].a != lines[ previous ].a ) {
            intersect( lines[ i ], lines[ previous ], points[ number ] );
            for ( ; points[ number ][ 0 ] < points[ number - 1 ][ 0 ]; --number ) {
                intersect( lines[index[number - 2]], lines[i], points[number - 1]);
            }
            previous = index[ number++ ] = i;
        }
    }
    points[ number ][ 0 ] = 10000000.0;
    points[ number ][ 1 ] = evaluate( lines[ previous ], points[ number ][ 0 ] );
    return ++number;
}

/* Find the intersect point for two non-parallel lines */
void intersect( Line l1, Line l2, double point[] )
{
    point[ 0 ] = ( (double)l1.b - l2.b ) / ( l2.a - l1.a );
    point[ 1 ] = evaluate( l1, point[ 0 ] );
}

/* Comparator: Lines with smaller slope first.
 *             For lines with equal slope, prefer larger intercept */
int cmp( const void *a, const void *b )
{
    const Line *l1 = a, *l2 = b;
    return ((l1->a < l2->a) || (l1->a == l2->a && l1->b > l2->b)) ? -1 : 1;
}

/* Get the y coordinate for a line with x-coordinate x */
double evaluate( Line l, double x )
{
    return l.a * x + l.b;
}

int main( void )
{
    int     A[] = { -1, 1, 0 }, B[] = { 3, 0, 2 };
    printf( "%f\n", solution( A, B, sizeof(A) / sizeof(A[0]) ) );
}
