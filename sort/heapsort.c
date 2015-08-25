#include <stdio.h>

void heapsort(int a[], int n);
void fixDown(int a[], int k, int n);

/* Heap sort */
void heapsort(int a[], int n)
{
    /* Build a max-heap */
    for (int i = n / 2 - 1; i >= 0; --i)
        fixDown(a, i, n);
    /* Iteratively extract the maximum from the heap*/
    for (; n-- > 1; fixDown(a, 0, n)) {
        int tmp = a[0];
        a[0] = a[n];
        a[n] = tmp;
    }
}

/* Fix the heap with n elements from the root */
void fixDown(int a[], int root, int n)
{
    /* The possible children of root are 2*root + 1 and 2*root + 2 */
    for (int maxchild; (maxchild = 2 * root + 1) < n; root = maxchild) {
        if (maxchild + 1 < n && a[maxchild] < a[maxchild + 1] )
            ++maxchild;
        if (a[root] >= a[maxchild])
            break;
        int tmp = a[root];
        a[root] = a[maxchild];
        a[maxchild] = tmp;
    }
}

int main( void )
{
    int     a[ 6 ] = { 1, 5, 3, 9, 7, 11 };

    heapsort( a, 6 );
    for ( int i = 0; i < 6; ++i )
        printf( "%d ", a[ i ] );
    return 0;
}
