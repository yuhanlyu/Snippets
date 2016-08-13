#include "josephus.h"

#include "gtest/gtest.h"

namespace {

static constexpr int32_t n = 2000000;

TEST(JosephusTest, ValidateShamsBaragh) {
    for (int32_t m = 2; m < n; m += 100000) {
        EXPECT_EQ(shams_baragh(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateWoodhousea) {
    for (int32_t m = 2; m < n; m += 100000) {
        EXPECT_EQ(woodhousea(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgi) {
    for (int32_t m = 2; m < n; m += 100000) {
        EXPECT_EQ(gelgi(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgiImprove) {
    for (int32_t m = 2; m < n; m += 100000) {
        EXPECT_EQ(gelgi_improve(n, m), taocp_k(n, m, n));
    }
}

TEST(JosephusTest, ValidateGelgiTAOCP) {
    for (int32_t m = 2; m < n; m += 100000) {
        EXPECT_EQ(taocp(n, m), taocp_k(n, m, n));
    }
}

}
