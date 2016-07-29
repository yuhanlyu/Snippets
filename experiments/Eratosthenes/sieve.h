#ifndef SIEVE_H_
#define SIEVE_H_

#include <stdint.h>
#include <stdbool.h>

static inline uint32_t number_to_index(uint32_t n) {
    return (n - 2) >> 1;
}

static inline bool is_prime(uint32_t n, const uint8_t prime[]) {
    return (n & 1) == 0 ? (n == 2) : (prime[number_to_index(n)] != 0);
}

void sieve(uint32_t n, uint8_t prime[]);

// This improvement is from Chapter 13 in Algorithms Unplugged.
void improved_sieve(uint32_t n, uint8_t prime[]);

// This is Pritchard's linear sieve method from the following paper:
// Paul Pritchard
// Linear prime-number sieves: A family tree
// Science of Computer Programming 
// Volume 9, Issue 1, August 1987, Pages 17-35
void linear_sieve(uint32_t n, uint8_t prime[]);

// Segmented sieve method from the following paper:
// Carter Bays and Richard H. Hudson
// The segmented sieve of eratosthenes and primes in 
// arithmetic progressions to 10^12
// BIT Numerical Mathematics June 1977, Volume 17, Issue 2, pp 121–127
void segmented_sieve(uint32_t n, uint8_t prime[]);

static inline uint64_t number_to_bit_index(uint64_t n) {
    return (n - 2) >> 1;
}

static inline bool bit_get(uint64_t x, const uint32_t bitset[]) {
    return (bitset[x>>5] & (1 << (x&31))) != 0;
}

static inline bool is_prime_bit(uint64_t n, const uint32_t bitset[]) {
    return (n & 1) == 0 ? (n == 2) : 
           (bit_get(number_to_bit_index(n), bitset) != 0);
}

void sieve_bit(uint64_t n, uint32_t prime[]);

void improved_sieve_bit(uint64_t n, uint32_t prime[]);

void linear_sieve_bit(uint64_t n, uint32_t prime[]);

void segmented_sieve_bit(uint64_t n, uint32_t prime[]);

static inline uint64_t wheel_index(uint64_t n) {
    return (n << 2) / 15;
}

static inline bool is_prime_wheel(uint64_t n, const uint32_t bitset[]) {
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0)
        return n == 2 || n == 3 || n == 5;
    return bit_get(wheel_index(n), bitset);
}

// Wheel sieve.
// More details can be found in the following paper:
// Paul Pritchard
// Explaining the wheel sieve
// Acta Informatica October 1982, Volume 17, Issue 4, pp 477 - 485
void wheel_bit(uint64_t n, uint32_t prime[]);

// Segmented wheel sieve
void segmented_wheel_bit(uint64_t n, uint32_t prime[]);

// The upper bound of the number of primes at most n.
// This formula is from the following paper:
// Pierre Dusart,
// The $k^{th}$ prime is greater than $k(\ln k +\ln\ln k -1)$ for $k\geq 2$,
// Mathematics of Computation, 8(225): 411-415 (1999)
uint32_t upper_bound_of_pi(uint32_t n) {
    return (n / log(n)) * (1 + 1.2762 / log(n));
}
#endif
