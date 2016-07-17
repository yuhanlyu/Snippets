#include "sieve.h"

#include <algorithm>
#include <cstdint>

#include "benchmark/benchmark_api.h"

namespace {

static constexpr int32_t size = 1 << 28;
static constexpr int32_t bitset_size = 1 << 30;
static constexpr int32_t m = 16;
uint8_t prime[size + 1];
uint32_t prime_bit[bitset_size / 32 + 1];

static void Sieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve(state.range_x(), prime);
    }
}
BENCHMARK(Sieve)->RangeMultiplier(m)->Range(1024, size);

static void SieveImprove(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_improve(state.range_x(), prime);
    }
}
BENCHMARK(SieveImprove)->RangeMultiplier(m)->Range(1024, size);

static void SieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_bit(state.range_x(), prime_bit);
    }
}
BENCHMARK(SieveBitset)->RangeMultiplier(m)->Range(1024, bitset_size);

static void SieveImproveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve_improve_bit(state.range_x(), prime_bit);
    }
}
BENCHMARK(SieveImproveBitset)->RangeMultiplier(m)->Range(1024, bitset_size);
}

BENCHMARK_MAIN();
