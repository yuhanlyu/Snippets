#include "fib.h"

#include "gtest/gtest.h"

namespace {

const int max = 92;
int64_t ans[max + 1];

class FibonacciTest : public ::testing::Test {
  protected:
    static void SetUpTestCase() {
        for (int i = 1; i <= max; ++i) {
            ans[i] = iterative(i);
        }
    }
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
