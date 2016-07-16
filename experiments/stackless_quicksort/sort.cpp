#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <algorithm>
#define TEST_LENGTH 500000

int compare(const void *p, const void *q);
int compare(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

void quick(int a[], int end);

/* Quicksort: sort the array a[2..end-1], where end < length of A - 1
 * This algorithm is from Lutz M. Wegner's paper 
 * "A generalized, one-way, stackless quicksort," 
 * BIT Numerical Mathematics 1987, Volume 27, Issue 1, pp 44-48
 */
void quick(int A[], int end)
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

/* Fix the heap with n elements from the root */
void fixDown(int a[], int root, int n);
void fixDown(int a[], int root, int n)
{
    /* The possible children of root are 2*root + 1 and 2*root + 2 */
    for (int maxchild; (maxchild = (root << 1) + 1) < n; root = maxchild) {
        if (maxchild + 1 < n && a[maxchild] < a[maxchild + 1] )
            ++maxchild;
        if (a[root] >= a[maxchild])
            break;
        int tmp = a[root];
        a[root] = a[maxchild];
        a[maxchild] = tmp;
    }
}

/* Heap sort */
void heapsort(int a[], int n);
void heapsort(int a[], int n)
{
    /* Build a max-heap */
    for (int i = (n >> 1) - 1; i >= 0; --i)
        fixDown(a, i, n);
    /* Iteratively extract the maximum from the heap*/
    for (; n-- > 1; fixDown(a, 0, n)) {
        int tmp = a[0];
        a[0] = a[n];
        a[n] = tmp;
    }
}

void time_used(struct timeval *t);
void time_used(struct timeval *t)
{
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    *t = ru.ru_utime;
}

int main(void)
{
    int test[TEST_LENGTH + 3] = {0};
    int test1[TEST_LENGTH + 3] = {0};
    int test2[TEST_LENGTH + 3] = {0};
    int test3[TEST_LENGTH + 3] = {0};
    srand(time(NULL));
    for (int i = 0; i < TEST_LENGTH; ++i) {
        test3[i + 2] = test2[i + 2] = test1[i + 2] = test[i + 2] = rand();
    }
    struct timeval t0, t1, t2, t3, t4, dt;
    time_used(&t0);
    qsort(test + 2, TEST_LENGTH, sizeof(int), compare);
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("qsort used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    std::sort(test + 2, test + 2 + TEST_LENGTH);
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("std::sort used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    quick(test2, TEST_LENGTH + 1);
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("Stackless qsort used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    heapsort(test3 + 2, TEST_LENGTH);
    time_used(&t4);
    timersub(&t4, &t3, &dt);
    printf("Heapsort used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int i = 0; i < TEST_LENGTH; ++i) {
        assert(test[i + 2] == test2[i + 2]);
        assert(test[i + 2] == test3[i + 2]);
    }
    return 0;
}
