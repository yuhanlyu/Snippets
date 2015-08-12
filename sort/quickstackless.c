#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <assert.h>

void quick(int a[], int begin, int end);

/* Quicksort: sort the array a[begin..end-1], where begin >= 2 
 *                                            and end < length of A - 1
 * This algorithm is from Lutz M. Wegner's paper 
 * "A generalized, one-way, stackless quicksort," 
 * BIT Numerical Mathematics 1987, Volume 27, Issue 1, pp 44-48
 */
void quick( int A[], int begin, int end )
{
    A[1] = A[end + 1] = INT_MIN;
    for (int left = 2; left <= end + 1;) {
        // A[left] is a stopper
        if (A[left] <= A[left - 1]) {
            A[left - 2] = A[left];
            left += 2;
            continue;
        }
        int i = left, j = left;
        for (int pivot = A[left]; ; A[j] = A[++i]) {
            // Find the next out of order position
            while (pivot < A[++j]) ;

            // A[j] is a stopeer, partition the current part is finished
            if (A[j] <= A[left - 1]) {
                A[i] = pivot;
                break;
            }

            // A[j] is not a stopper
            if (A[j] >= A[i - 1]) {
                A[i] = A[j]; // A[i] must be the maximum of the left part
            } else {
                A[i] = A[i - 1];
                A[i - 1] = A[j];
            }
        }
        if (left + 2 >= i) {
            A[left - 2] = A[j];
            A[j] = A[i - 1];
            left = i + 1;
        } else {
            int temp = A[i - 1];
            A[i - 1] = A[j];
            A[j] = temp;
        }
    }
}

int main( void )
{
    int     a[] = { 0, 0, 1, 4, 5, 2, 3, 0};
    int     b[100] = {0};

    quick(a, 2, 6);
    for (int i = 2; i <= 6; ++i)
        printf("%d ", a[i]);
    puts("");
    srand(time(NULL));
    for (int i = 2; i <= 98; ++i)
        b[i] = rand() % 1000;
    quick(b, 2, 98);
    for (int i = 2; i <= 98; ++i) {
        printf("%d ", b[i]);
        assert(i == 2 || b[i] >= b[i - 1]);
    }
    puts("");
    return 0;
}
