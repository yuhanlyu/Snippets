#include "rotation.h"

#include "benchmark/benchmark_api.h"

namespace {

const unsigned range = 1000000U;
unsigned temp[range];
unsigned shift = range / 17;

static void BM_JugglingBentley(benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_bentley(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}
BENCHMARK(BM_JugglingBentley);

static void BM_JugglingShene(benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_shene(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}
BENCHMARK(BM_JugglingShene);

static void BM_RotateReverse(benchmark::State& state) {
    while (state.KeepRunning()) {
        rotate_reverse(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}
BENCHMARK(BM_RotateReverse);

static void BM_BlockSwapShene(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_shene(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}
BENCHMARK(BM_BlockSwapShene);

static void BM_BlockSwapGries(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_gries(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}
BENCHMARK(BM_BlockSwapGries);

}
BENCHMARK_MAIN()
