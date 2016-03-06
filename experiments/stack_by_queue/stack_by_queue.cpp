#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>
#define TEST_LENGTH 500000U

// This solution is from Martin Hühne's paper
// “On the Power of Several Queues”. 
// In: Theoretical Computer Science 113.1 (May 1993), pages 75–91.
class Stack {
public:
    void push(int x) {
        first.emplace(x);
        for (int i = first.size() - 1; i > 0; --i) {
            first.emplace(first.front());
            first.pop();
        }
        if (first.size() * first.size() > second.size()) {
            while (!second.empty()) {
                first.emplace(second.front());
                second.pop();
            }
            first.swap(second);
        }
    }

    void pop() {
        !first.empty() ? first.pop() : second.pop();
    }

    int top() {
        return !first.empty() ? first.front() : second.front();
    }

    bool empty() {
        return first.empty() && second.empty();
    }
private:
    std::queue<int> first;
    std::queue<int> second;
};

void time_used(struct timeval *t);
void time_used(struct timeval *t)
{
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    *t = ru.ru_utime;
}

int main(void)
{
    int n = TEST_LENGTH;
    int a[TEST_LENGTH] = {0};
    bool push[TEST_LENGTH] = {false};
    volatile long ans = 0;

    srand(time(NULL));
    std::stack<int> stack1;
    Stack stack2;
    for (int i = 0; i < 1000; ++i) {
        if (rand() % 2 == 1) {
            int r = rand() % (2 * n);
            stack1.emplace(r);
            stack2.push(r);
            assert(stack1.top() == stack2.top());
        } else {
            if (!stack1.empty()) {
                assert(stack1.top() == stack2.top());
                stack1.pop();
                stack2.pop();
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        push[i] = rand() % 2 == 1;
        a[i] = rand() % (2 * n);
    }
    std::stack<int> stack3;
    Stack stack4;
    struct timeval t0, t1, t2, t3, dt;
    time_used(&t0);
    for (int k = 0; k < 100; ++k) {
        for (int i = 0; i < n; ++i)
            if (push[i]) {
                stack3.emplace(a[i]);
            } else if (!stack3.empty())
                stack3.pop();
    }
    time_used(&t1);
    timersub(&t1, &t0, &dt);
    printf("C++ stack used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    for (int k = 0; k < 100; ++k) {
        for (int i = 0; i < n; ++i)
            if (push[i]) {
                stack4.push(a[i]);
            } else if (!stack4.empty())
                stack4.pop();
    }
    time_used(&t2);
    timersub(&t2, &t1, &dt);
    printf("Simulated stack used %ld.%06d seconds\n", dt.tv_sec, dt.tv_usec);
    return 0;
}
