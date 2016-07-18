#include "sieve.h"

#include <algorithm>
#include <cstdint>

#include "benchmark/benchmark_api.h"

namespace {

static constexpr uint32_t size = 1U << 30;
static constexpr uint64_t bitset_size = 1LLU << 34;
static constexpr uint32_t bitset_size_limit = bitset_size >> 10;
static constexpr uint32_t m = 16;
uint8_t prime[size / 2];
uint32_t prime_bit[bitset_size / 64 + 1];

static void Sieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve(state.range_x(), prime);
    }
}
//BENCHMARK(Sieve)->RangeMultiplier(m)->Range(1024, size);

static void SieveImprove(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_improve(state.range_x(), prime);
    }
}
//BENCHMARK(SieveImprove)->RangeMultiplier(m)->Range(1024, size);

static void SieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        sieve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(SieveBitset)->RangeMultiplier(m)->Range(1, bitset_size_limit);

static void SieveImproveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        sieve_improve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(SieveImproveBitset)->RangeMultiplier(m)->Range(1, bitset_size_limit);
}

BENCHMARK_MAIN();
