#include "fib.h"

#include "gtest/gtest.h"

namespace {

unsigned ans[48];

class FibonacciTest : public ::testing::Test {
  protected:
    static void SetUpTestCase() {
        for (unsigned i = 1; i <= 47; ++i) {
            ans[i] = iterative(i);
        }
    }
};

TEST_F(FibonacciTest, ValidateDoubling) {
    for (unsigned i = 1; i <= 47; ++i) {
        EXPECT_EQ(ans[i], doubling(i));
    }
}

TEST_F(FibonacciTest, ValidateTumble) {
    for (unsigned i = 1; i <= 47; ++i) {
        EXPECT_EQ(ans[i], tumble(i));
    }
}

TEST_F(FibonacciTest, ValidateQMatrix) {
    for (unsigned i = 1; i <= 47; ++i) {
        EXPECT_EQ(ans[i], qmatrix(i));
    }
}

}
