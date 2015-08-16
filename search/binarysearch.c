#include <stdio.h>

/* Find the index of leftmost insertion x in a sorted array a 
 * with length n > 0 */
int binarysearch(int a[], int n, int x);
int binarysearch(int a[], int n, int x)
{
    int low = 0;
    for (int high = n - 1; low <= high; ) {
        int mid = low + ((high - low) / 2);
        if (a[mid] >= x)
            high = mid - 1;
        else
            low = mid + 1;
    } 
    return low;
}

int main( void )
{
    int     a[ 6 ] = { 0, 1, 3, 5, 7, 9 };

    printf("%d\n", binarysearch(a, 6, 2));
    return 0;
}
