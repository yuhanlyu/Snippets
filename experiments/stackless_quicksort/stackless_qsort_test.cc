#include "stackless_qsort.h"

#include <algorithm>
#include <limits>

#include "gtest/gtest.h"

namespace {

class QSortTest : public ::testing::Test {
  protected:
    virtual void SetUp() override {
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

int compare(const void *p, const void *q) {
    int x = *(const int *)p;
    int y = *(const int *)q;
    return (x == y) ? 0 : ((x < y) ? -1 : 1);
}

TEST_F(QSortTest, StacklessQSort) {
    int32_t temp[size + 1];
    int32_t answer[size + 1];

    std::copy(test + 2, test + size + 1, temp + 2);
    stackless_qsort(temp, size);

    std::copy(test + 2, test + size + 1, answer + 2);
    std::stable_sort(answer + 2, answer + size);

    for (int32_t i = 2; i < size; ++i) {
        EXPECT_EQ(temp[i], answer[i]);
    }
}

}
