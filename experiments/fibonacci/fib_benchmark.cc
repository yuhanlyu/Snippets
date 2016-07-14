#include "fib.h"

#include "benchmark/benchmark_api.h"

namespace {

static void BM_Iterative(benchmark::State& state) {
    while (state.KeepRunning()) {
       benchmark::DoNotOptimize(iterative(state.range_x()));
    }
}
BENCHMARK(BM_Iterative)->Arg(44)->Arg(45)->Arg(46)->Arg(47);

static void BM_Doubling(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(doubling(state.range_x()));
    }
}
BENCHMARK(BM_Doubling)->Arg(44)->Arg(45)->Arg(46)->Arg(47);

static void BM_Tumble(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(tumble(state.range_x()));
    }
}
BENCHMARK(BM_Tumble)->Arg(44)->Arg(45)->Arg(46)->Arg(47);

static void BM_QMatrix(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(qmatrix(state.range_x()));
    }
}
BENCHMARK(BM_QMatrix)->Arg(44)->Arg(45)->Arg(46)->Arg(47);

}

BENCHMARK_MAIN()
