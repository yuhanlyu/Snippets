# Implement the following operations of a stack using queues.
# Time Complexity: amortized O(sqrt(n)) for push, O(1) for others
# Space Complexity: O(n)
# http://cstheory.stackexchange.com/questions/2562/one-stack-two-queues

from collections import deque
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.first = deque()
        self.second = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.first.append(x)
        for _ in xrange(len(self.first) - 1):
            self.first.append(self.first.popleft())
        if len(self.first) * len(self.first) > len(self.second):
            while self.second:
                self.first.append(self.second.popleft())
            self.first, self.second = self.second, self.first

    # @return nothing
    def pop(self):
        return self.first.popleft() if self.first else self.second.popleft()

    # @return an integer
    def top(self):
        return self.first[0] if self.first else self.second[0]

    # @return an boolean
    def empty(self):
        return not self.first and not self.second

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print stack.top()
    print stack.pop()
