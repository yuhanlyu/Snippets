#include "binary_search.h"

#include "gtest/gtest.h"

namespace {

class SearchTest : public ::testing::Test {
  protected:
    void SetUp() override {
        for (int32_t i = 0; i < size; ++i)
            test[i] = 2 * i + 1;
    }
    static constexpr int32_t size = 1 << 20;
    int32_t test[size];
};

TEST_F(SearchTest, ValidateBinarySearch) {
    for (int32_t i = 0; i <= 2 * size; ++i)
        EXPECT_EQ(binary_search(test, size, i), i / 2);
}

TEST_F(SearchTest, ValidateBiasedSearch) {
    for (int32_t i = 0; i <= 2 * size; ++i)
        EXPECT_EQ(biased_search(test, size, i), i / 2);
}

TEST_F(SearchTest, ValidateSizeSpecializedSearch) {
    for (int32_t i = 0; i < size; ++i)
        EXPECT_EQ(size_specialized_search(test, size, 2 * i + 1), i);
}

}
