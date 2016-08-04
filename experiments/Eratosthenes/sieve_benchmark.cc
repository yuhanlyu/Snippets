#include "sieve.h"

#include <algorithm>
#include <cstdint>

#include "benchmark/benchmark_api.h"

namespace {

static constexpr uint32_t size = 1U << 30;
static constexpr uint64_t bitset_size = 1LLU << 34;
static constexpr uint32_t bitset_size_limit = bitset_size >> 10;
static constexpr uint32_t m = 2;
bool prime[size / 2];
uint32_t prime_bit[bitset_size / 64 + 1];

static void Sieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        sieve(state.range_x(), prime);
    }
}
BENCHMARK(Sieve)->RangeMultiplier(m)->Range(1024, size);

static void ImprovedSieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        improved_sieve(state.range_x(), prime);
    }
}
BENCHMARK(ImprovedSieve)->RangeMultiplier(m)->Range(1024, size);

static void LinearSieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        linear_sieve(state.range_x(), prime);
    }
}
BENCHMARK(LinearSieve)->RangeMultiplier(m)->Range(1024, size);

static void SegmentedSieve(benchmark::State& state) {
    while (state.KeepRunning()) {
        segmented_sieve(state.range_x(), prime);
    }
}
BENCHMARK(SegmentedSieve)->RangeMultiplier(m)->Range(1024, size);

static void SieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        sieve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(SieveBitset)->RangeMultiplier(m)->Range(1, bitset_size_limit);

static void ImprovedSieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        improved_sieve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(ImprovedSieveBitset)->RangeMultiplier(m)->Range(1, bitset_size_limit);

static void LinearSieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        linear_sieve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(LinearSieveBitset)->RangeMultiplier(m)->Range(1, bitset_size_limit);

static void SegmentedSieveBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        segmented_sieve_bit(n << 10, prime_bit);
    }
}
BENCHMARK(SegmentedSieveBitset)
    ->RangeMultiplier(m)->Range(1, bitset_size_limit);

static void WheelBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        wheel_bit(n << 10, prime_bit);
    }
}
BENCHMARK(WheelBitset)->RangeMultiplier(m)
    ->Range(1, bitset_size_limit);

static void SegmentedWheelBitset(benchmark::State& state) {
    while (state.KeepRunning()) {
        int64_t n = state.range_x();
        segmented_wheel_bit(n << 10, prime_bit);
    }
}
BENCHMARK(SegmentedWheelBitset)->RangeMultiplier(m)
    ->Range(1, bitset_size_limit);
}

BENCHMARK_MAIN();
