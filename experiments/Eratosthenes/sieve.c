#include "sieve.h"

#include <math.h>
#include <string.h>

void sieve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n / 2);
    uint32_t bound = round(sqrt(n));
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t j = i * i; j <= n; j += 2 * i) {
                prime[number_to_index(j)] = 0;
            }
        }
    }
}

void sieve_improve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n / 2);
    uint32_t bound = round(sqrt(n));
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t k = n / i - ((n / i) % 2 == 0), j = i * k; 
                         k >= i; k -= 2, j -= 2 * i) {
                if (prime[number_to_index(k)]) {
                    prime[number_to_index(j)] = 0;
                }
            }
        }
    }
}

// Number of bytes having at least n + 1 bits
static inline uint64_t bytes(uint64_t n) {
    return (n / 2) / 8 + ((n / 2) % 8 == 0 ? 0 : 1);
}

static inline void reset(uint64_t x, uint32_t bitset[]) { 
    x = number_to_bit_index(x);
    bitset[x>>5] &= ~(1 << (x&31));
}

void sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = roundl(sqrtl(n));
    for (uint64_t i = 3; i <= bound; i += 2) {
        if (get(i, prime)) {
            for (uint64_t j = i * i; j <= n; j += 2 * i) {
                reset(j, prime);
            }
        }
    }
}

void sieve_improve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = roundl(sqrtl(n));
    for (uint64_t i = 3; i <= bound; i += 2) {
        if (get(i, prime)) {
            for (uint64_t k = n / i - ((n / i) % 2 == 0), j = i * k; 
                         k >= i; k -= 2, j -= 2 * i) {
                if (get(k, prime))
                    reset(j, prime);
            }
        }
    }
}
