#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#define TEST_LENGTH 500000U
#define QUERY_LENGTH 500000U

/* Find the index of leftmost insertion x in a sorted array a 
 * with length n > 0 */
long binarysearch(int a[], long n, int x);
long binarysearch(int a[], long n, int x)
{
    long low = 0;
    for (long high = n - 1; low <= high; ) {
        long mid = low + ((high - low) >> 1);
        if (a[mid] >= x)
            high = mid - 1;
        else
            low = mid + 1;
    } 
    return low;
}

// Not use middle value
long biasedsearch(int a[], long n, int x);
long biasedsearch(int a[], long n, int x)
{
    long low = 0;
    for (long high = n - 1; low <= high; ) {
        long mid = low + ((high - low) >> 2);
        if (a[mid] >= x)
            high = mid - 1;
        else
            low = mid + 1;
    } 
    return low;
}

int compare(const void *p, const void *q);
int compare(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
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
    int n = TEST_LENGTH, qn = QUERY_LENGTH;
    int a[TEST_LENGTH] = {0};
    int q[QUERY_LENGTH] = {0};
    volatile long ans = 0;

    srand(time(NULL));
    for (int i = 0; i < n; ++i)
        a[i] = rand() % (2 * n);
    qsort(a, n, sizeof(int), compare);
    for (int i = 0; i < qn; ++i) {
        q[i] = rand() % (2 * n);
        assert(binarysearch(a, n, q[i]) == biasedsearch(a, n, q[i]));
        auto low = std::lower_bound(a, a + n, q[i]);
        assert(binarysearch(a, n, q[i]) == low - a);
    }
    struct timeval t0, t1, t2, t3, dt;
    time_used(&t0);
    for (int k = 0; k < 100; ++k) {
        for (int i = 0; i < qn; ++i)
            ans = binarysearch(a, n, q[i]);
    }
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Ordinary method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int k = 0; k < 100; ++k) {
        for (int i = 0; i < qn; ++i)
            ans = biasedsearch(a, n, q[i]);
    }
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Biased method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int k = 0; k < 100; ++k) {
        for (int i = 0; i < qn; ++i)
            ans = std::lower_bound(a, a + n, q[i]) - a;
    }
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("C++ lower_bound used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    return 0;
}
