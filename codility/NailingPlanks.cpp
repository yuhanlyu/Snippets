#include <iostream>
#include <vector>
#include <limits>
#include <deque>

// Time complexity is O(M + N)
int solution(std::vector<int> &A, std::vector<int> &B, std::vector<int> &C);
int solution(std::vector<int> &A, std::vector<int> &B, std::vector<int> &C)
{
    std::vector<int> nail(2 * C.size() + 1, std::numeric_limits<int>::max());  
    std::vector<int> left(2 * C.size() + 1);
    for (int i = C.size() - 1; i >= 0; --i)
        nail[C[i]] = i;
    for (int i = 0; i < A.size(); ++i)
        left[B[i]] = std::max(A[i], left[B[i]]);
    std::deque<int> q;
    int l = 0, r = 0, result = 0;
    for (int i = 1; i < 2 * C.size() + 1; ++i) {
        if (left[i] > l) {
            for (l = left[i]; !q.empty() && q.front() < l; q.pop_front()) ;
            for (r = std::max(r, l); r <= i; q.emplace_back(r++))
                for (; !q.empty() && nail[q.back()] >= nail[r]; q.pop_back()) ;
            result = std::max(result, nail[q.front()]);
            if (result == std::numeric_limits<int>::max())
                return -1;
        }
    }
    return result + 1;
}

int main(void)
{
    std::vector<int> A({1, 4, 5, 8});
    std::vector<int> B({4, 5, 9, 10});
    std::vector<int> C({4, 6, 7, 10, 2});
    std::cout << solution(A, B, C) << '\n';
    return 0;
}
