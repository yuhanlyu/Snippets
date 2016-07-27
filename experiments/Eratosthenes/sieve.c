#include "sieve.h"

#include <math.h>
#include <string.h>

void sieve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t j = i * i; j <= n; j += (i << 1)) {
                prime[number_to_index(j)] = 0;
            }
        }
    }
}

void improved_sieve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    for (uint32_t i = 3; i <= bound; i += 2) {
        if (prime[number_to_index(i)]) {
            for (uint32_t k = n / i - (((n / i) & 1) == 0), j = i * k; 
                         k >= i; k -= 2, j -= (i << 1) ) {
                if (prime[number_to_index(k)]) {
                    prime[number_to_index(j)] = 0;
                }
            }
        }
    }
}

// The upper bound of the number of primes at most n.
// This formula is from the following paper:
// Pierre Dusart, 
// The $k^{th}$ prime is greater than $k(\ln k +\ln\ln k -1)$ for $k\geq 2$,
// Mathematics of Computation, 8(225): 411-415 (1999)
uint32_t upper_bound_of_pi(uint32_t n) {
    return (n / log(n)) * (1 + 1.2762 / log(n));
}

void linear_sieve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    sieve(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (prime[number_to_index(i)])
            primes[number_of_primes++] = i;
    for (uint32_t i = 3; i <= n / 3; i += 2) {
        for (uint32_t j = 0; j < number_of_primes && primes[j] <= n / i; ++j) {
            prime[number_to_index(primes[j] * i)] = 0;
            if (i % primes[j] == 0)
                break;
        }
    }
}

void segmented_sieve(uint32_t n, uint8_t prime[]) {
    memset(prime, 1, n >> 1);
    uint32_t bound = sqrt(n);
    sieve(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (prime[number_to_index(i)])
            primes[number_of_primes++] = i;
    for (uint32_t low = bound + 1, high = 2 * bound; low <= n; low += bound) {
        for (uint32_t h = 0; h < number_of_primes; ++h) {
            uint32_t i = primes[h], j = ((low + (i - 1)) / i) * i;
            for (j += i * ((j & 1) == 0); j <= high; j += (i << 1)) {
                prime[number_to_index(j)] = 0;
            }
        }
        high = (high + bound > n) ? n : high + bound;
    }
}

// Number of bytes having at least n + 1 bits
static inline uint64_t bytes(uint64_t n) {
    return (n >> 4) + (((n >> 1) & 7) != 0);
}

static inline void reset(uint64_t x, uint32_t bitset[]) { 
    x = number_to_bit_index(x);
    bitset[x>>5] &= ~(1 << (x&31));
}

void sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    for (uint64_t i = 3; i <= bound; i += 2) {
        if (get(i, prime)) {
            for (uint64_t j = i * i; j <= n; j += 2 * i) {
                reset(j, prime);
            }
        }
    }
}

void improved_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
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

void linear_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    sieve_bit(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (get(i, prime))
            primes[number_of_primes++] = i;
    for (uint64_t i = 3; i <= n / 3; i += 2) {
        for (uint32_t j = 0; j < number_of_primes && primes[j] <= n / i; ++j) {
            reset(primes[j] * i, prime);
            if (i % primes[j] == 0)
                break;
        }
    }
}

void segmented_sieve_bit(uint64_t n, uint32_t prime[]) {
    memset(prime, 0xFF, bytes(n));
    uint64_t bound = sqrtl(n);
    sieve_bit(bound, prime);
    uint32_t primes[upper_bound_of_pi(bound)], number_of_primes = 0;
    for (uint32_t i = 3; i <= bound; i += 2)
        if (get(i, prime))
            primes[number_of_primes++] = i;
    for (uint64_t low = bound + 1, high = 2 * bound; low <= n; low += bound) {
        for (uint64_t h = 0; h < number_of_primes; ++h) {
            uint64_t i = primes[h], j = ((low + (i - 1)) / i) * i;
            for (j += i * ((j & 1) == 0); j <= high; j += (i << 1)) {
                reset(j, prime);
            }
        }
        high = (high + bound > n) ? n : high + bound;
    }
}
