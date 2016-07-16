#include "stackless_qsort.h"

#include <algorithm>
#include <cstdlib>
#include <limits>

#include "benchmark/benchmark_api.h"

namespace {

class QSortBenchmark : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        test[0] = test[1] = test[size] = 0;
        int32_t x = 1;
        for (int32_t i = 0; i < size - 2; ++i) {
            test[i + 2] = x;
            x = x * 48271 % std::numeric_limits<std::int32_t>::max();
            if (x < 0)
                x = -x;
        }
    }

    static constexpr int32_t size = 1000000;
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
