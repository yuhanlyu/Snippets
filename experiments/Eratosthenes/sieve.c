#include <stdio.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#define MAX 200000000

void eratosthenes(char prime[], int n);
void eratosthenes(char prime[], int n)
{
    memset(prime, 1, n + 1);
    prime[0] = prime[1] = 0;
    int bound = round(sqrt(n));
    for (int i = 2; i <= bound; ++i) {
        if (prime[i]) {
            for (int j = i * i; j <= n; j += i)
                prime[j] = 0;
        }
    }
}

void eratosthenes2(char prime[], int n);
void eratosthenes2(char prime[], int n)
{
    memset(prime, 1, n + 1);
    prime[0] = prime[1] = 0;
    int bound = round(sqrt(n));
    for (int i = 2; i <= bound; ++i) {
        if (prime[i]) {
            for (int k = n / i, j = i * k; k >= i; --k, j -= i)
                if (prime[k])
                    prime[j] = 0;
        }
    }
}

void time_used(struct timeval *t);
void time_used(struct timeval *t)
{
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    *t = ru.ru_utime;
}


char prime[MAX + 1], prime2[MAX + 1];
int main(void)
{
    struct timeval t0, t1, t2, dt;
    time_used(&t0);
    eratosthenes(prime, MAX);
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("Ordinary method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    eratosthenes2(prime2, MAX);
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Modified method used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int i = 1; i <= MAX; ++i)
        assert(prime[i] == prime2[i]);
}
