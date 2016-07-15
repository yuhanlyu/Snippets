#include "josephus.h"

#include "benchmark/benchmark_api.h"

namespace {

const int n = 2000000;
const int m = 100000;

static void BM_ShamsBaragh(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(shams_baragh(n, m));
    }
}
BENCHMARK(BM_ShamsBaragh);

static void BM_Woodhousea(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(woodhousea(n, m));
    }
}
BENCHMARK(BM_Woodhousea);

static void BM_Gelgi(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(gelgi(n, m));
    }
}
BENCHMARK(BM_Gelgi);

static void BM_GelgiImprove(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(gelgi_improve(n, m));
    }
}
BENCHMARK(BM_GelgiImprove);

static void BM_TAOCP(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(taocp(n, m));
    }
}
BENCHMARK(BM_TAOCP);

static void BM_TAOCPK(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(taocp_k(n, m, n));
    }
}
BENCHMARK(BM_TAOCPK);

}
BENCHMARK_MAIN();
