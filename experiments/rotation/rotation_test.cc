#include "rotation.h"

#include "gtest/gtest.h"

namespace {

const unsigned size = 1000000U;
const unsigned cases = 10U;
unsigned shift[cases];

class RotationTest : public ::testing::Test {
  protected:
    static void SetUpTestCase() {
        srand(time(NULL));
        for (unsigned i = 0; i < cases; ++i) {
            shift[i] = rand() % size;
        }
    }
    virtual void SetUp() override {
        for (unsigned i = 0; i < size; ++i) {
            test[i] = i;
        }
    }
    unsigned test[size];
};

TEST_F(RotationTest, ValidateJugglingBently) {
    for (unsigned i = 0; i < cases; ++i) {
        unsigned temp[size];
        memcpy(temp, test, size * sizeof(int));
        juggling_bentley(temp, size, shift[i]);
        for (unsigned j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateJugglingShene) {
    for (unsigned i = 0; i < cases; ++i) {
        unsigned temp[size];
        memcpy(temp, test, size * sizeof(int));
        juggling_shene(temp, size, shift[i]);
        for (unsigned j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateRotateReverse) {
    for (unsigned i = 0; i < cases; ++i) {
        unsigned temp[size];
        memcpy(temp, test, size * sizeof(int));
        rotate_reverse(temp, size, shift[i]);
        for (unsigned j = 0; j < size; ++j) {
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
        }
    }
}

TEST_F(RotationTest, ValidateBlockSwapShene) {
    for (unsigned i = 0; i < cases; ++i) {
        unsigned temp[size];
        memcpy(temp, test, size * sizeof(int));
        block_swap_shene(temp, size, shift[i]);
        for (unsigned j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

TEST_F(RotationTest, ValidateBlockSwapGries) {
    for (unsigned i = 0; i < cases; ++i) {
        unsigned temp[size];
        memcpy(temp, test, size * sizeof(int));
        block_swap_gries(temp, size, shift[i]);
        for (unsigned j = 0; j < size; ++j)
            ASSERT_EQ(temp[j], (j + shift[i]) % size);
    }
}

}
