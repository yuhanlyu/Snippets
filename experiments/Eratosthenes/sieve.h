#ifndef SIEVE_H_
#define SIEVE_H_

#include <cstdint>

void sieve(int32_t n, uint8_t prime[]);

// This improvement is from Chapter 13 in Algorithms Unplugged.
void sieve_improve(int32_t n, uint8_t prime[]);

void sieve_bit(int32_t n, uint32_t prime[]);

void sieve_improve_bit(int32_t n, uint32_t prime[]);
#endif
