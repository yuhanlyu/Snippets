#ifndef SIEVE_H_
#define SIEVE_H_

#include <cstdint>
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

static inline int32_t get(uint32_t x, uint32_t bitset[]) {
    x = number_to_index(x);
    return (bitset[x>>5] >> (x&31)) & 1;
}

static inline bool is_prime_bit(uint32_t n, uint32_t bitset[]) {
    return n % 2 == 0 ? (n == 2) : (get(n, bitset) == 1);
}

void sieve_bit(uint32_t n, uint32_t prime[]);

void sieve_improve_bit(uint32_t n, uint32_t prime[]);
#endif
