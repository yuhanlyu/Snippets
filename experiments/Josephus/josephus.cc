#include "josephus.h"

#include <stack>

int32_t shams_baragh(int64_t n, int32_t m) {
    int64_t d = 1;
    while (d <= (m - 1) * n)
        d = (m * d) / (m - 1) + ((m * d) % (m - 1) != 0);
    return m * n + 1 - d;
}

int32_t woodhousea(int32_t n, int32_t m) {
    int32_t ans = 0;
    for (int32_t i = 2; i <= n; ++i)
        ans = (ans + m) % i;
    return ans + 1;
}

int32_t gelgi(int32_t n, int32_t m) {
    std::stack<std::tuple<int32_t, int32_t, int32_t>> stack;
    stack.emplace(n, m, 0);
    int32_t value = 0;
    while (!stack.empty()) {
        std::tuple<int32_t, int32_t, int32_t> r = stack.top();
        stack.pop();
        n = std::get<0>(r); 
        m = std::get<1>(r);
        if (std::get<2>(r) == 0) {
            if (n <= m) {
                for (int32_t i = 2; i <= n; ++i)
                    value = (value + m) % i;
                ++value;
            } else {
                stack.emplace(n, m, 1);
                stack.emplace(n - n / m, m, 0);
            }
        } else {
            if (value <= n % m)
                value += (n / m) * m;
            else {
                value -= n % m;
                int32_t k = value % (m - 1);
                value = (value / (m - 1)) * m + (k == 0 ? -1 : k);
            }
        }
    }
    return value;
}

int32_t gelgi_improve(int32_t n, int32_t m) {
    int32_t nn = n, ans = 0, iterations = 1, top = 0;
    std::stack<int32_t> mark;

    for (iterations = 1; nn > m << 3; ++iterations) {
        int p = nn;
        nn -= nn / m;
        if (nn + nn / (m - 1) - p == 1)
            mark.emplace(iterations);
    }
    for (int32_t i = 2; i <= nn; ++i)
        ans = (ans + m) % i;
    for (++ans, --iterations; nn != n; --iterations) {
        nn += nn / (m - 1);
        if (!mark.empty() && mark.top() == iterations) {
            mark.pop();
            --nn;
        }
        if (ans <= nn % m)
            ans += (nn / m) * m;
        else {
            ans -= nn % m;
            int32_t k = ans % (m - 1);
            ans = (ans / (m - 1)) * m + (k == 0 ? -1 : k);
        }
    }
    return ans;
}

int32_t taocp(int32_t n, int32_t m) {
    int64_t answer = (int64_t)n * m;
    while (answer > n)
        answer += (answer - n - 1) / (m - 1) - n;
    return answer;
}

int32_t taocp_k(int32_t n, int32_t m, int32_t k) {
    int64_t answer = (int64_t)k * m;
    while (answer > n)
        answer = answer - n + (answer - n - 1) / (m - 1);
    return answer;
}
