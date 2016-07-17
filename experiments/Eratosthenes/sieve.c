#include "sieve.h"

#include <string.h>
#include <math.h>

void sieve(int32_t n, uint8_t prime[]) {
    memset(prime, 1, n + 1);
    prime[0] = prime[1] = 0;
    int32_t bound = round(sqrt(n));
    for (int32_t i = 2; i <= bound; ++i) {
        if (prime[i]) {
            for (int32_t j = i * i; j <= n; j += i)
                prime[j] = 0;
        }
    }
}

void sieve_improve(int32_t n, uint8_t prime[]) {
    memset(prime, 1, n + 1);
    prime[0] = prime[1] = 0;
    int32_t bound = round(sqrt(n));
    for (int32_t i = 2; i <= bound; ++i) {
        if (prime[i]) {
            for (int32_t k = n / i, j = i * k; k >= i; --k, j -= i)
                if (prime[k])
                    prime[j] = 0;
        }
    }
}

static inline int32_t get(uint32_t bitset[], int x) { 
    return (bitset[x>>5] >> (x&31)) & 1;
}

static inline void reset(uint32_t bitset[], int x) { 
    bitset[x>>5] &= ~(1 << (x&31));
}

// Number of bytes having at least n + 1 bits
static inline int32_t bytes(int32_t n) {
    return (n + 1) / 8 + ((n + 1) % 8 == 0 ? 0 : 1);
}

void sieve_bit(int32_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    reset(prime, 0);
    reset(prime, 1);
    int32_t bound = round(sqrt(n));
    for (int32_t i = 2; i <= bound; ++i) {
        if (get(prime, i)) {
            for (int32_t j = i * i; j <= n; j += i)
                reset(prime, j);
        }
    }
}

void sieve_improve_bit(int32_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    reset(prime, 0);
    reset(prime, 1);
    int32_t bound = round(sqrt(n));
    for (int32_t i = 2; i <= bound; ++i) {
        if (get(prime, i)) {
            for (int32_t k = n / i, j = i * k; k >= i; --k, j -= i)
                if (get(prime, k))
                    reset(prime, j);
        }
    }
}
