#include "binary_search.h"

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <random>

#include "benchmark/benchmark_api.h"

namespace {

class SearchBenchmark : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        generator.seed();
        for (int32_t i = 0; i < state.range_x(); ++i) {
            test[i] = distribution(generator);
        }
        std::sort(test, test + state.range_x());
    }
    static constexpr int32_t size  = 1 << 20;
    static constexpr int32_t max = INT32_MAX;
    std::uniform_int_distribution<int32_t> distribution{0, max};
    std::default_random_engine generator;
    int32_t test[size];
};

BENCHMARK_DEFINE_F(SearchBenchmark, Random)(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(distribution(generator));
    }
}
BENCHMARK_REGISTER_F(SearchBenchmark, Random)
    ->Arg(1 << 20);

BENCHMARK_DEFINE_F(SearchBenchmark, BinarySearch)(benchmark::State& state) {
    for (int32_t r = 0; state.KeepRunning(); ) {
        r = distribution(generator);
        benchmark::DoNotOptimize(binary_search(test, state.range_x(), r));
    }
}
BENCHMARK_REGISTER_F(SearchBenchmark, BinarySearch)
    ->RangeMultiplier(4)->Range(1 << 10, 1 << 20);

BENCHMARK_DEFINE_F(SearchBenchmark, BiasedSearch)(benchmark::State& state) {
    for (int32_t r = 0; state.KeepRunning(); ) {
        r = distribution(generator);
        benchmark::DoNotOptimize(biased_search(test, state.range_x(), r));
    }
}
BENCHMARK_REGISTER_F(SearchBenchmark, BiasedSearch)
    ->RangeMultiplier(4)->Range(1 << 10, 1 << 20);

BENCHMARK_DEFINE_F(SearchBenchmark, STLSearch)(benchmark::State& state) {
    for (int32_t r = 0; state.KeepRunning(); ) {
        r = distribution(generator);
        benchmark::DoNotOptimize(std::lower_bound(test, 
                                                  test + state.range_x(), r));
    }
}
BENCHMARK_REGISTER_F(SearchBenchmark, STLSearch)
    ->RangeMultiplier(4)->Range(1 << 10, 1 << 20);

int compare(const void *p, const void *q) {
    int32_t x = *(const int32_t *)p;
    int32_t y = *(const int32_t *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

BENCHMARK_DEFINE_F(SearchBenchmark, BSearch)(benchmark::State& state) {
    for (int32_t r = 0; state.KeepRunning(); ) {
        r = distribution(generator);
        benchmark::DoNotOptimize(bsearch(&r, test, state.range_x(), 
                                         sizeof(int32_t), compare));
    }
}
BENCHMARK_REGISTER_F(SearchBenchmark, BSearch)
    ->RangeMultiplier(4)->Range(1 << 10, 1 << 20);

}

BENCHMARK_MAIN();
