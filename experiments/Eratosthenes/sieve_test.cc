#include "sieve.h"

#include <cstdint>

#include "gtest/gtest.h"

namespace {

static constexpr int32_t size = 1000000;

TEST(SieveTest, SieveImprove) {
    uint8_t prime1[size + 1];
    uint8_t prime2[size + 1];

    sieve(size, prime1);
    sieve_improve(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(prime1[i], prime2[i]);
    }
}

static inline int32_t get(uint32_t bitset[], int32_t x) {
    return (bitset[x>>5] >> (x&31)) & 1;
}

TEST(SieveTest, SieveBitset) {
    static constexpr int32_t size = 1000000;
    uint8_t prime1[size + 1];
    uint32_t prime2[(size + 1) / 32 + 1];

    sieve(size, prime1);
    sieve_bit(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(prime1[i], get(prime2, i));
    }
}

TEST(SieveTest, SieveImproveBitset) {
    uint8_t prime1[size + 1];
    uint32_t prime2[(size + 1) / 32 + 1];

    sieve(size, prime1);
    sieve_improve_bit(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(prime1[i], get(prime2, i));
    }
}

}
