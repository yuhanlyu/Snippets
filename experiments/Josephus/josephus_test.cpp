#include "josephus.h"

#include "gtest/gtest.h"

namespace {

TEST(JosephusTest, ValidateShamsBaragh) {
    const int32_t n = 2000000;
    for (int32_t m = 100000; m < n; m += 100000) {
        EXPECT_EQ(shams_baragh(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateWoodhousea) {
    const int32_t n = 2000000;
    for (int32_t m = 100000; m < n; m += 100000) {
        EXPECT_EQ(woodhousea(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgi) {
    const int32_t n = 2000000;
    for (int32_t m = 100000; m < n; m += 100000) {
        EXPECT_EQ(gelgi(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgiImprove) {
    const int32_t n = 2000000;
    for (int32_t m = 100000; m < n; m += 100000) {
        EXPECT_EQ(gelgi_improve(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgiTAOCP) {
    const int32_t n = 2000000;
    for (int32_t m = 100000; m < n; m += 100000) {
        EXPECT_EQ(taocp(n, m), taocp_k(n, m, n));
    }
}

}
