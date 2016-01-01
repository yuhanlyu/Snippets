#include <stdio.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>

// Armin Shams-Baragh's method
int josephus(long long n, int m);
int josephus(long long n, int m)
{
    long long d = 1;
    while (d <= (m - 1) * n) {
        d = (m * d) / (m - 1) + ((m * d) % (m - 1) != 0);
    }
    return m * n + 1 - d;
}

// O(n) algorithm
// D. Woodhousea, "Programming the Josephus problem," 
// ACM SIGCSE Bulletin, Volume 10 Issue 4, December 1978 Pages 56-58 
int josephus0(int n, int m);
int josephus0(int n, int m)
{
    int ans = 0;
    for (int i = 2; i <= n; ++i)
        ans = (ans + m) % i;
    return ans + 1;
}

// Fatih Gelgi's method in "Time Improvement on Josephus Problem"
// Since this is a recursive algorith, stack may overflow.
int josephus1(int n, int m);
int josephus1(int n, int m)
{
    if (n <= m)
        return josephus0(n, m);
    int jn = josephus1(n - n / m, m);
    if (jn <= n % m)
        return jn + (n / m) * m;
    jn -= n % m;
    int k = jn % (m - 1);
    return (jn / (m - 1)) * m + (k == 0 ? -1 : k);
}

// Method from TAOCP
int josephus2(int n, int m);
int josephus2(int n, int m)
{
    long long answer = (long long)n * m;
    while (answer > n)
        answer += (answer - n - 1) / (m - 1) - n;
    return answer;
}

// Method from TAOCP
int josephus2k(int n, int m, int k);
int josephus2k(int n, int m, int k)
{
    long long answer = (long long)k * m;
    while (answer > n)
        answer = answer - n + (answer - n - 1) / (m - 1);
    return answer;
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
    const int n = 2000000;
    volatile int ans = 0;

    for (int m = 100000; m < n; m += 100000) {
        int a = josephus(n, m), b = josephus1(n, m);
        int c = josephus2(n, m), d = josephus2k(n, m, n);
        assert(a == b);
        assert(b == c);
        assert(c == d);
    }
    printf("Start\n");

    struct timeval t0, t1, t2, t3, dt;
    time_used(&t0);
    for (int m = 100000; m < n; m += 100000) {
        ans = josephus(n, m);
    }
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Armin Shams-Baragh's method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int m = 10000; m < n; m += 100000) {
        ans = josephus1(n, m);
    }
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Fatih Gelgi's method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int m = 10000; m < n; m += 100000) {
        ans = josephus2(n, m);
    }
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("TAOCP method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    return 0;
}
