#ifndef SIEVE_H_
#define SIEVE_H_

#include <stdint.h>
#include <stdbool.h>

static inline uint32_t number_to_index(uint32_t n) {
    return (n - 2) / 2;
}

static inline bool is_prime(uint32_t n, uint8_t prime[]) {
    return n % 2 == 0 ? (n == 2) : (prime[number_to_index(n)] == 1);
}

void sieve(uint32_t n, uint8_t prime[]);

// This improvement is from Chapter 13 in Algorithms Unplugged.
void sieve_improve(uint32_t n, uint8_t prime[]);

static inline uint64_t number_to_bit_index(uint64_t n) {
    return (n - 2) / 2;
}

static inline bool get(uint64_t x, uint32_t bitset[]) {
    x = number_to_bit_index(x);
    return (bitset[x>>5] >> (x&31)) & 1;
}

static inline bool is_prime_bit(uint64_t n, uint32_t bitset[]) {
    return n % 2 == 0 ? (n == 2) : (get(n, bitset) == 1);
}

void sieve_bit(uint64_t n, uint32_t prime[]);

void sieve_improve_bit(uint64_t n, uint32_t prime[]);
#endif
