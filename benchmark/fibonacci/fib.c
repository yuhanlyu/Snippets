#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#define TEST_LENGTH 500000U

/* Computing Fibonacci number by using 
 * F(2n) = F(n)^2 + F(n+1)^2 and F(2n+1) = 2F(n)F(n+1) + F(n+1)^2
 * This algorithm is from Joseph Shortt's paper
 * "An interative program to calculate fibonacci numbers in O(log n) arithmetic 
 * operations," Information Processing Letters Volume 7, Issue 6, 
 * October 1978, Pages 299-303 */
unsigned int doubling(unsigned int n);
unsigned int doubling(unsigned int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    unsigned int j, nn = n;
    for (j = 0; nn > 0; nn >>= 1, ++j) ;
    unsigned int s1 = 0, s2 = 1;
    for (int k = j - 2; k >= 0; --k) {
        unsigned t = s2 * s2, s2k = s1 * s1 + t, s2k1 = t + ((s1 * s2) << 1);
        if ((n >> k) & 1) {
            s1 = s2k1;
            s2 = s2k + s2k1;
        } else {
            s1 = s2k;
            s2 = s2k1;
        }
    }
    return s2;
}

/* This function computes the n-th fibonacci number, where n should be a 
 * non-negative number
 * This algorithm is from L.F. Johnsonn's paper:
 * "Tumble, a fast simple iteration algorithm for Fibonacci,"
 * Information Processing Letters Volume 89, Issue 4, 28 February 2004, 
 * Pages 187–189 */
unsigned int fibonacci(unsigned int n);
unsigned int fibonacci(unsigned int n) 
{
    unsigned int even = 0, odd = 1, i;

    /* even is the i-th fibonacci number
       odd is the (i+1)-th fibonacci number */
    for ( i = 0; i < n; i += 2 ) {
        odd += even;
        even += odd;
    }
    return i == n ? even : odd;
}

// Ordinary way of computing fibonacci number
unsigned int iterative(unsigned int n);
unsigned int iterative(unsigned int n)
{
    unsigned int first = 0, second = 1;
    for (unsigned k = 0; k < n; ++k)
    {
        unsigned t = first + second;
        first = second;
        second = t;
    }
    return first;
}

// Q-matrix method
unsigned int qmatrix(unsigned int n);
unsigned int qmatrix(unsigned int n)
{
    unsigned int a = 1, b = 0, c = 0, d = 1;
    for (--n; n > 0; n >>= 1) {
        if (n & 1){
            unsigned int t = d * (b + a) + c * b;
            a = d * b + c * a;
            b = t;
        }
        unsigned int t = d *((c << 1) + d);
        c = c * c + d * d;
        d = t;
    }
    return a + b;
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
    unsigned max = 47;  // Maximum parameter for unsigned 32-bit integer
    unsigned shift = 3; // The range of testing is [shift, max]
    unsigned test[TEST_LENGTH] = {0};
    unsigned answer[TEST_LENGTH] = {0};
    unsigned result[TEST_LENGTH] = {0};
    unsigned int volatile ans;
    srand(time(NULL));
    for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
        test[i] = shift + 1 + rand() % (max - shift);
        assert(shift <= test[i] && test[i] <= max);
    }
    struct timeval t0, t1, t2, t3, t4, dt;
    time_used(&t0);
    for (unsigned int j = 0; j < 100; ++j) {
        for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
            ans = iterative(test[i]);
        }
    }
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Iterative method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned int j = 0; j < 100; ++j) {
        for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
            ans = fibonacci(test[i]);
        }
    }
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Tumble method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned int j = 0; j < 100; ++j) {
        for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
            ans = qmatrix(test[i]);
        }
    }
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("Qmatrix method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned int j = 0; j < 100; ++j) {
        for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
            ans = doubling(test[i]);
        }
    }
    time_used(&t4);
    timersub(&t4, &t3, &dt);
    printf("Doubling method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
        answer[i] = iterative(test[i]);
    }
    for (unsigned int i = 0; i < TEST_LENGTH; ++i) {
        result[i] = fibonacci(test[i]);
        assert(result[i] == answer[i]);
        result[i] = qmatrix(test[i]);
        assert(result[i] == answer[i]);
        result[i] = doubling(test[i]);
        assert(result[i] == answer[i]);
    }
    return 0;
}
