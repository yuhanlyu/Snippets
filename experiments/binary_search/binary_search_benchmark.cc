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
        for (int32_t i = 0; i < size; ++i) {
            test[i] = distribution(generator);
        }
        std::sort(test, test + size);
    }
    static constexpr int32_t size  = 1000000;
    static constexpr int32_t max = INT32_MAX;
    static constexpr int32_t m = max / size;
    std::uniform_int_distribution<int32_t> distribution =
        std::uniform_int_distribution<int32_t>(0, max);
    std::default_random_engine generator;
    int32_t test[size];
};

BENCHMARK_F(SearchBenchmark, Random)(benchmark::State& state) {
    while (state.KeepRunning()) {
        benchmark::DoNotOptimize(distribution(generator));
    }
}

BENCHMARK_F(SearchBenchmark, BinarySearch)(benchmark::State& state) {
    for (int32_t r = distribution(generator); state.KeepRunning(); 
         r = distribution(generator)) {
        benchmark::DoNotOptimize(binary_search(test, size, r));
    }
}

BENCHMARK_F(SearchBenchmark, BiasedSearch)(benchmark::State& state) {
    for (int32_t r = distribution(generator); state.KeepRunning(); 
         r = distribution(generator)) {
        benchmark::DoNotOptimize(biased_search(test, size, r));
    }
}

BENCHMARK_F(SearchBenchmark, STLSearch)(benchmark::State& state) {
    for (int32_t r = distribution(generator); state.KeepRunning(); 
         r = distribution(generator)) {
        benchmark::DoNotOptimize(std::lower_bound(test, test + size, r));
    }
}

int compare(const void *p, const void *q) {
    int32_t x = *(const int32_t *)p;
    int32_t y = *(const int32_t *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

BENCHMARK_F(SearchBenchmark, BSearch)(benchmark::State& state) {
    for (int32_t r = distribution(generator); state.KeepRunning(); 
         r = distribution(generator)) {
        benchmark::DoNotOptimize(bsearch(&r, test, size, sizeof(int32_t),
                                         compare));
    }
}

}

BENCHMARK_MAIN();
