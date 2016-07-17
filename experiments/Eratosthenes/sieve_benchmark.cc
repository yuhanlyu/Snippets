#include "sieve.h"

#include <algorithm>
#include <cstdint>

#include "benchmark/benchmark_api.h"

namespace {

class Sieve : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        std::fill(prime, prime + size + 1, false);
    }

    static constexpr int32_t size = 100000000;
    static constexpr int32_t bitset_size = size * 10;
    static constexpr int32_t m = 10;
    uint8_t prime[size + 1];
    uint32_t prime_bit[bitset_size / 8 + 1];
};

BENCHMARK_DEFINE_F(Sieve, Ordinary)(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve(state.range_x(), prime);
    }
}
BENCHMARK_REGISTER_F(Sieve, Ordinary)
    ->RangeMultiplier(Sieve::m)->Range(1000, Sieve::size);

BENCHMARK_DEFINE_F(Sieve, SieveImprove)(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_improve(state.range_x(), prime);
    }
}
BENCHMARK_REGISTER_F(Sieve, SieveImprove)
    ->RangeMultiplier(Sieve::m)->Range(1000, Sieve::size);

BENCHMARK_DEFINE_F(Sieve, SieveBitset)(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_bit(state.range_x(), prime_bit);
    }
}
BENCHMARK_REGISTER_F(Sieve, SieveBitset)
    ->RangeMultiplier(Sieve::m)
    ->Range(1000, Sieve::bitset_size);

BENCHMARK_DEFINE_F(Sieve, SieveImproveBitset)(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_improve_bit(state.range_x(), prime_bit);
    }
}
BENCHMARK_REGISTER_F(Sieve, SieveImproveBitset)
    ->RangeMultiplier(Sieve::m)
    ->Range(1000, Sieve::bitset_size);
}

BENCHMARK_MAIN();
