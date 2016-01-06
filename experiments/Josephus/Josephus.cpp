#include <stdio.h>
#include <stack>
#include <tuple>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>

// Armin Shams-Baragh's method
int josephus(long long n, int m);
int josephus(long long n, int m)
{
    long long d = 1;
    while (d <= (m - 1) * n)
        d = (m * d) / (m - 1) + ((m * d) % (m - 1) != 0);
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
// I modified the recursive algorithm in the paper to be a iterative one.
// O(m + lg_{m/(m-1)} (n/m))
int josephus1(int n, int m);
int josephus1(int n, int m)
{
    std::stack<std::tuple<int, int, int>> stack;
    stack.emplace(n, m, 0);
    int value = 0;
    while (!stack.empty()) {
        std::tuple<int, int, int> r = stack.top();
        stack.pop();
        n = std::get<0>(r); 
        m = std::get<1>(r); 
        if (std::get<2>(r) == 0) {
            if (n <= m) {
                for (int i = 2; i <= n; ++i)
                    value = (value + m) % i;
                ++value;
            } else {
                stack.emplace(n, m, 1);
                stack.emplace(n - n / m, m, 0);
            }
        } else {
            if (value <= n % m)
                value += (n / m) * m;
            else {
                value -= n % m;
                int k = value % (m - 1);
                value = (value / (m - 1)) * m + (k == 0 ? -1 : k);
            }
        }
    }
    return value;
}

// My space-efficient version of Gelgi's method
int josephus1a(int n, int m);
int josephus1a(int n, int m)
{
    int nn = n, ans = 0, iterations = 1;
    std::stack<int> mark;

    for (iterations = 1; nn > m; ++iterations) {
        int p = nn;
        nn -= nn / m;
        if (nn + nn / (m - 1) - p == 1)
            mark.emplace(iterations);
    }
    for (int i = 2; i <= nn; ++i)
        ans = (ans + m) % i;
    for (++ans, --iterations; nn != n; --iterations) {
        nn += nn / (m - 1);
        if (!mark.empty() && mark.top() == iterations) {
            mark.pop();
            --nn;
        }
        if (ans <= nn % m)
            ans += (nn / m) * m;
        else {
            ans -= nn % m;
            int k = ans % (m - 1);
            ans = (ans / (m - 1)) * m + (k == 0 ? -1 : k);
        }
    }
    return ans;
}

// Method from TAOCP
// O(log_{m/(m-1)} n(m-1))
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
        int z = josephus1a(n, m);
        int a = josephus(n, m), b = josephus1(n, m);
        int c = josephus2(n, m), d = josephus2k(n, m, n);
        assert(z == a);
        assert(a == b);
        assert(b == c);
        assert(c == d);
    }
    printf("Start\n");

    struct timeval t0, t1, t2, t3, t4, dt;
    time_used(&t0);
    for (int m = 100000; m < n; m += 100000) {
        ans = josephus(n, m);
    }
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Shams-Baragh's method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int m = 10000; m < n; m += 100000) {
        ans = josephus2(n, m);
    }
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("TAOCP method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int m = 10000; m < n; m += 100000) {
        ans = josephus1(n, m);
    }
    time_used(&t3);
    timersub(&t3, &t2, &dt);
    printf("Gelgi's method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int m = 10000; m < n; m += 100000) {
        ans = josephus1a(n, m);
    }
    time_used(&t4);
    timersub(&t4, &t3, &dt);
    printf("Space efficient method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    return 0;
}
