#ifndef SIEVE_H_
#define SIEVE_H_

#include <stdint.h>
#include <stdbool.h>

bool is_prime(uint32_t n, const bool prime[]);

void sieve(uint32_t n, bool prime[]);

// This improvement is from Chapter 13 in Algorithms Unplugged.
void improved_sieve(uint32_t n, bool prime[]);

// This is Pritchard's linear sieve method from the following paper:
// Paul Pritchard
// Linear prime-number sieves: A family tree
// Science of Computer Programming 
// Volume 9, Issue 1, August 1987, Pages 17-35
void linear_sieve(uint32_t n, bool prime[]);

// Segmented sieve method from the following paper:
// Carter Bays and Richard H. Hudson
// The segmented sieve of eratosthenes and primes in 
// arithmetic progressions to 10^12
// BIT Numerical Mathematics June 1977, Volume 17, Issue 2, pp 121 - 127
void segmented_sieve(uint32_t n, bool prime[]);

bool is_prime_bit(uint64_t n, const uint32_t bitset[]);

void sieve_bit(uint64_t n, uint32_t prime[]);

void improved_sieve_bit(uint64_t n, uint32_t prime[]);

void linear_sieve_bit(uint64_t n, uint32_t prime[]);

void segmented_sieve_bit(uint64_t n, uint32_t prime[]);

bool is_prime_wheel(uint64_t n, const uint32_t bitset[]);

// Wheel sieve.
// More details can be found in the following paper:
// Paul Pritchard
// Explaining the wheel sieve
// Acta Informatica October 1982, Volume 17, Issue 4, pp 477 - 485
void wheel_bit(uint64_t n, uint32_t prime[]);

// Segmented wheel sieve
void segmented_wheel_bit(uint64_t n, uint32_t prime[]);

#endif
