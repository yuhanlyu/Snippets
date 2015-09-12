#include <stdio.h>
#include <stdlib.h>
#include <functional>
#include <numeric>
#include <valarray>
#include <time.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#define TEST_LENGTH 500000U

double sum(double a[], int n);
double sum(double a[], int n)
{
    double ans = 0.0;
    for (int i = 0; i < n; ++i)
        ans += a[i];
    return ans;
}

double sum2(double a[], int n);
double sum2(double a[], int n)
{
    double even = 0.0, odd = 0.0;
    for (int i = 0; i + 1 < n; i += 2) {
        even += a[i];
        odd += a[i + 1];
    }
    return even + odd + (n & 1 ? a[n - 1] : 0.0);
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
    int n = TEST_LENGTH;
    double a[TEST_LENGTH] = {0};
    volatile double ans = 0;

    srand(time(NULL));
    for (int i = 0; i < n; ++i)
        a[i] = (rand() % 10000) / 10000.0;
    std::valarray<double> array(a, n);
    printf("%f %f %f %f\n", sum(a, n), sum2(a, n), array.sum(), 
                            std::accumulate(a, a + n, 0.0));
    struct timeval t0, t1, t2, t3, t4, dt;
    time_used(&t0);
    for (int i = 0; i < 10000; ++i)
        ans = sum(a, n);
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Ordinary method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int i = 0; i < 10000; ++i)
        ans = sum2(a, n);
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Modified method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int i = 0; i < 10000; ++i)
        ans = std::accumulate(a, a + n, 0.0);
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("std::accumulate used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int i = 0; i < 10000; ++i)
        ans = array.sum();
    time_used(&t4);
    timersub(&t4, &t3, &dt);
    printf("std::valarray.sum used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
}
