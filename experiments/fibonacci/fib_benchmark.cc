#include "fib.h"

#include "benchmark/benchmark_api.h"

namespace {

constexpr int32_t n = 92;

static void BM_Iterative(benchmark::State& state) {
    while (state.KeepRunning()) {
       benchmark::DoNotOptimize(iterative(n));
    }
}
BENCHMARK(BM_Iterative);

static void BM_Doubling(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(doubling(n));
    }
}
BENCHMARK(BM_Doubling);

static void BM_Tumble(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(tumble(n));
    }
}
BENCHMARK(BM_Tumble);

static void BM_QMatrix(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(qmatrix(n));
    }
}
BENCHMARK(BM_QMatrix);

}

BENCHMARK_MAIN();
