#include "rotation.h"

#include "gtest/gtest.h"

namespace {

class RotationTest : public ::testing::Test {
  protected:
    static void SetUpTestCase() {
        srand(time(NULL));
        for (int32_t i = 0; i < cases; ++i) {
            shift[i] = rand() % size;
        }
    }
    virtual void SetUp() override {
        for (int32_t i = 0; i < size; ++i) {
            test[i] = i;
        }
    }
    static constexpr int32_t size = 1000000;
    static constexpr int32_t cases = 10;
    static int32_t shift[cases];
    int32_t test[size];
};

int32_t RotationTest::shift[cases];

TEST_F(RotationTest, ValidateJugglingBently) {
    for (int32_t i = 0; i < cases; ++i) {
        int32_t temp[size];
        memcpy(temp, test, size * sizeof(int));
        juggling_bentley(temp, size, shift[i]);
        for (int32_t j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateJugglingShene) {
    for (int32_t i = 0; i < cases; ++i) {
        int32_t temp[size];
        memcpy(temp, test, size * sizeof(int));
        juggling_shene(temp, size, shift[i]);
        for (int32_t j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateRotateReverse) {
    for (int32_t i = 0; i < cases; ++i) {
        int32_t temp[size];
        memcpy(temp, test, size * sizeof(int));
        rotate_reverse(temp, size, shift[i]);
        for (int32_t j = 0; j < size; ++j) {
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
        }
    }
}

TEST_F(RotationTest, ValidateBlockSwapShene) {
    for (int32_t i = 0; i < cases; ++i) {
        int32_t temp[size];
        memcpy(temp, test, size * sizeof(int));
        block_swap_shene(temp, size, shift[i]);
        for (int32_t j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateBlockSwapGries) {
    for (int32_t i = 0; i < cases; ++i) {
        int32_t temp[size];
        memcpy(temp, test, size * sizeof(int));
        block_swap_gries(temp, size, shift[i]);
        for (int32_t j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

}
