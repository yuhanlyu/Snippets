#include "sieve.h"

#include <cstdint>

#include "gtest/gtest.h"

namespace {

static constexpr uint32_t size = 1 << 20;

TEST(SieveTest, ImprovedSieve) {
    uint8_t prime1[size / 2];
    uint8_t prime2[size / 2];

    sieve(size, prime1);
    improved_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, LinearSieve) {
    uint8_t prime1[size / 2];
    uint8_t prime2[size / 2];

    sieve(size, prime1);
    linear_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, SegmentedSieve) {
    uint8_t prime1[size / 2];
    uint8_t prime2[size / 2];

    sieve(size, prime1);
    segmented_sieve(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime(i, prime2));
    }
}

TEST(SieveTest, SieveBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, ImprovedSieveBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    improved_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, LinearSieveBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    linear_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, SegmentedSieveBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    segmented_sieve_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_bit(i, prime2));
    }
}

TEST(SieveTest, WheelBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    wheel_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_wheel(i, prime2));
    }
}

TEST(SieveTest, SegmentedWheelBitset) {
    uint8_t prime1[size / 2];
    uint32_t prime2[size / 64 + 1];

    sieve(size, prime1);
    segmented_wheel_bit(size, prime2);
    for (uint32_t i = 2; i <= size; ++i) {
        EXPECT_EQ(is_prime(i, prime1), is_prime_wheel(i, prime2)) << i;
    }
}

}
