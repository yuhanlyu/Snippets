#include "fib.h"

#include "gtest/gtest.h"

namespace {

class FibonacciTest : public ::testing::Test {
  protected:
    virtual void SetUp() override {
        for (int i = 1; i <= max; ++i) {
            ans[i] = iterative(i);
        }
    }
    static constexpr int32_t max = 92;
    int64_t ans[max + 1];
};

TEST_F(FibonacciTest, ValidateDoubling) {
    for (int i = 1; i <= max; ++i) {
        EXPECT_EQ(ans[i], doubling(i));
    }
}

TEST_F(FibonacciTest, ValidateTumble) {
    for (int i = 1; i <= max; ++i) {
        EXPECT_EQ(ans[i], tumble(i));
    }
}

TEST_F(FibonacciTest, ValidateQMatrix) {
    for (int i = 1; i <= max; ++i) {
        EXPECT_EQ(ans[i], qmatrix(i));
    }
}

}
