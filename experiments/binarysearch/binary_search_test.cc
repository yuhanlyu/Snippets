#include "binary_search.h"

#include "gtest/gtest.h"

namespace {
const int32_t size = 10000000;
int32_t test[size];

class SearchTest : public ::testing::Test {
  protected:
    static void SetUpTestCase() {
        for (int32_t i = 0; i < size; ++i)
            test[i] = i;
    }
};

TEST_F(SearchTest, ValidateBinarySearch) {
    for (int32_t i = 0; i < size; ++i)
        EXPECT_EQ(binary_search(test, size, i), i);
}

TEST_F(SearchTest, ValidateBiasedSearch) {
    for (int32_t i = 0; i < size; ++i)
        EXPECT_EQ(biased_search(test, size, i), i);
}

}
