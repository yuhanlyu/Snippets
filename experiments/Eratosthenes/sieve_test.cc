#include "sieve.h"

#include <cstdint>

#include "gtest/gtest.h"

namespace {

static constexpr uint32_t size = 1 << 20;

TEST(SieveTest, ImprovedSieve) {
    bool prime1[size / 2];
    bool prime2[size / 2];

    sieve(size, prime1);
    improved_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, LinearSieve) {
    bool prime1[size / 2];
    bool prime2[size / 2];

    sieve(size, prime1);
    linear_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, SegmentedSieve) {
    bool prime1[size / 2];
    bool prime2[size / 2];

    sieve(size, prime1);
    segmented_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, SieveBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, ImprovedSieveBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    improved_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, LinearSieveBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    linear_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, SegmentedSieveBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    segmented_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, WheelBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    wheel_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_wheel(i, prime2));
    }
}

TEST(SieveTest, SegmentedWheelBitset) {
    bool prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    segmented_wheel_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_wheel(i, prime2)) << i;
    }
}

}
