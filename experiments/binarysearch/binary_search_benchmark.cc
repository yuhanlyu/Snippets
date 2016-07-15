#include "binary_search.h"

#include <algorithm>
#include <stdlib.h>

#include "benchmark/benchmark_api.h"

namespace {

class SearchBenchmark : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        for (int32_t i = 0; i < size; ++i) {
            test[i] = i * m;
        }
    }
    static constexpr int32_t size  = 100000000;
    static constexpr int32_t prime = 100001177;
    static constexpr int32_t m = 2000000000 / size;
    int32_t test[size];
};

BENCHMARK_F(SearchBenchmark, BinarySearch)(benchmark::State& state) {
    for (int32_t i = 0; state.KeepRunning(); i = (i + prime) % (size * m)) {
        benchmark::DoNotOptimize(binary_search(test, size, i));
    }
}

BENCHMARK_F(SearchBenchmark, BiasedSearch)(benchmark::State& state) {
    for (int32_t i = 0; state.KeepRunning(); i = (i + prime) % (size * m)) {
        benchmark::DoNotOptimize(biased_search(test, size, i));
    }
}

BENCHMARK_F(SearchBenchmark, STLSearch)(benchmark::State& state) {
    for (int32_t i = 0; state.KeepRunning(); i = (i + prime) % (size * m)) {
        benchmark::DoNotOptimize(std::lower_bound(test, test + size, i));
    }
}

int compare(const void *p, const void *q) {
    int32_t x = *(const int32_t *)p;
    int32_t y = *(const int32_t *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

BENCHMARK_F(SearchBenchmark, BSearch)(benchmark::State& state) {
    for (int32_t i = 0; state.KeepRunning(); i = (i + prime) % (size * m)) {
        benchmark::DoNotOptimize(bsearch(&i, test, size, sizeof(int32_t),
                                         compare));
    }
}

}

BENCHMARK_MAIN();
