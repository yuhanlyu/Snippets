#include <stdio.h>
#include <string.h>
#include <math.h>

// In order to get 100, finding primes first is necessary
int solution(int N);
int solution(int N)
{
    int l = log2(N) + 1, s = sqrt(N) + 1, top = 0, result = 1, top2 = 0;
    int factors[l], sieve[s], primes[s];
    memset(factors, 0, sizeof(int) * (l));
    memset(sieve, 0, sizeof(int) * (s));
    memset(primes, 0, sizeof(int) * (s));
    for (int i = 2; i * i < s; ++i) {
        if (sieve[i] == 0) {
            for (int j = i * i; j < s; j += i)
                sieve[j] = 1;
        }
    }
    for (int i = 2; i < s; ++i ) {
        if (sieve[i] == 0)
            primes[top++] = i;
    }
    for (int i = 0; i < top; ++i) {
        if (N % primes[i] == 0) {
            for (; N % primes[i] == 0; N /= primes[i])
                ++factors[top2];
            ++top2;
        }
    }
    if (N > 1)
        factors[top2++] = 1;
    for (int i = 0; i < top2; ++i)
        result *= (factors[i] + 1);
    return result;
}

int main(void)
{
    printf("%d\n", solution(24));
    printf("%d\n", solution(69));
    printf("%d\n", solution(2147483647));
    return 0;
}
