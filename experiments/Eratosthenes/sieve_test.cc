#include "sieve.h"

#include <cstdint>

#include "gtest/gtest.h"

namespace {

static constexpr int32_t size = 1000000;

TEST(SieveTest, SieveImprove) {
    uint8_t prime1[size / 2];
    uint8_t prime2[size / 2];

    sieve(size, prime1);
    sieve_improve(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, SieveBitset) {
    static constexpr int32_t size = 1000000;
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    sieve_bit(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, SieveImproveBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    sieve_improve_bit(size, prime2);
    for (int32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

}
