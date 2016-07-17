#include "stackless_qsort.h"

#include <algorithm>
#include <cstdlib>
#include <cstdint>
#include <random>

#include "benchmark/benchmark_api.h"

namespace {

class QSortBenchmark : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        generator.seed();
        test[0] = test[1] = test[size] = 0;
        for (int32_t i = 0; i < size - 2; ++i) {
            test[i + 2] = distribution(generator);
        }
    }

    static constexpr int32_t size = 1000000;
    static constexpr int32_t max = INT32_MAX;
    std::uniform_int_distribution<int32_t> distribution{0, max};
    std::default_random_engine generator;
    int32_t test[size + 1];
};

BENCHMARK_F(QSortBenchmark, StacklessQSort)(benchmark::State& state) {
    while (state.KeepRunning()) {
        int32_t temp[size + 1];
        std::copy(test + 2, test + size + 1, temp + 2);
        stackless_qsort(temp, size);
    }
}

BENCHMARK_F(QSortBenchmark, STLQSort)(benchmark::State& state) {
    while (state.KeepRunning()) {
        int32_t temp[size + 1];
        std::copy(test + 2, test + size + 1, temp + 2);
        std::sort(temp + 2, temp + size);
    }
}

BENCHMARK_F(QSortBenchmark, STLStableQSort)(benchmark::State& state) {
    while (state.KeepRunning()) {
        int32_t temp[size + 1];
        std::copy(test + 2, test + size + 1, temp + 2);
        std::stable_sort(temp + 2, temp + size);
    }
}

int32_t compare(const void *p, const void *q) {
    int32_t x = *(const int32_t *)p;
    int32_t y = *(const int32_t *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

BENCHMARK_F(QSortBenchmark, QSort)(benchmark::State& state) {
    while (state.KeepRunning()) {
        int32_t temp[size + 1];
        std::copy(test + 2, test + size + 1, temp + 2);
        qsort(temp + 2, size - 2, sizeof(int32_t), compare);
    }
}

}

BENCHMARK_MAIN();
