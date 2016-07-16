#include "rotation.h"

#include "benchmark/benchmark_api.h"

namespace {

class Rotation : public benchmark::Fixture {
  public:
    void SetUp(const ::benchmark::State& state) {
        for (int32_t i = 0; i < range; ++i)
            temp[i] = i;
    }
    static constexpr int32_t range = 1000000;
    static constexpr int32_t multiplier = 6561;
    int32_t temp[range];
};

BENCHMARK_DEFINE_F(Rotation, JugglingBentley)
    (benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_bentley(temp, range, state.range_x());
    }
}
BENCHMARK_REGISTER_F(Rotation, JugglingBentley)
    ->RangeMultiplier(Rotation::multiplier)->Range(1, Rotation::range - 1);

BENCHMARK_DEFINE_F(Rotation, JugglingShene)(benchmark::State& state) {
    while (state.KeepRunning()) {
        juggling_shene(temp, range, state.range_x());
    }
}
BENCHMARK_REGISTER_F(Rotation, JugglingShene)
    ->RangeMultiplier(Rotation::multiplier)->Range(1, Rotation::range - 1);

BENCHMARK_DEFINE_F(Rotation, RotateReverse)(benchmark::State& state) {
    while (state.KeepRunning()) {
        rotate_reverse(temp, range, state.range_x());
    }
}
BENCHMARK_REGISTER_F(Rotation, RotateReverse)
    ->RangeMultiplier(Rotation::multiplier)->Range(1, Rotation::range - 1);

BENCHMARK_DEFINE_F(Rotation, BlockSwapShene)(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_shene(temp, range, state.range_x());
    }
}
BENCHMARK_REGISTER_F(Rotation, BlockSwapShene)
    ->RangeMultiplier(Rotation::multiplier)->Range(1, Rotation::range - 1);

BENCHMARK_DEFINE_F(Rotation, BlockSwapGries)(benchmark::State& state) {
    while (state.KeepRunning()) {
        block_swap_gries(temp, range, state.range_x());
    }
}
BENCHMARK_REGISTER_F(Rotation, BlockSwapGries)
    ->RangeMultiplier(Rotation::multiplier)->Range(1, Rotation::range - 1);

}
BENCHMARK_MAIN();
