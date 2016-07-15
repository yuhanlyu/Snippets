#include "rotation.h"

#include "benchmark/benchmark_api.h"

namespace {

class RotationBenchmark : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        for (int32_t i = 0; i < range; ++i)
            temp[i] = i;
    }
    static constexpr int32_t range = 1000000;
    static constexpr int32_t shift = range / 17;
    int32_t temp[range];
};

BENCHMARK_F(RotationBenchmark, JugglingBentley)(benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_bentley(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}

BENCHMARK_F(RotationBenchmark, JugglingShene)(benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_shene(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}

BENCHMARK_F(RotationBenchmark, RotateReverse)(benchmark::State& state) {
    while (state.KeepRunning()) {
        rotate_reverse(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}

BENCHMARK_F(RotationBenchmark, BlockSwapShene)(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_shene(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}

BENCHMARK_F(RotationBenchmark, BlockSwapGries)(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_gries(temp, range, shift);
    }
    benchmark::DoNotOptimize(temp[0]);
}

}
BENCHMARK_MAIN();
