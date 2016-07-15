#include "fib.h"

#include "benchmark/benchmark_api.h"

namespace {

static void BM_Iterative(benchmark::State& state) {
    while (state.KeepRunning()) {
       benchmark::DoNotOptimize(iterative(92));
    }
}
BENCHMARK(BM_Iterative);

static void BM_Doubling(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(doubling(92));
    }
}
BENCHMARK(BM_Doubling);

static void BM_Tumble(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(tumble(92));
    }
}
BENCHMARK(BM_Tumble);

static void BM_QMatrix(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(qmatrix(92));
    }
}
BENCHMARK(BM_QMatrix);

}

BENCHMARK_MAIN()
