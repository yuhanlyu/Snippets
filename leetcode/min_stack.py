# Design a stack that supports push, pop, top, and retrieving the 
# minimum element in constant time.
# Time Complexity: O(1)
# Space Complexity: O(n)

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.min_values = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.min_values or x <= self.min_values[-1]:
            self.min_values.append(x)
    # @return nothing
    def pop(self):
        if self.stack[-1] == self.min_values[-1]:
            self.min_values.pop()
        return self.stack.pop()
    # @return an integer
    def top(self):
        return self.stack[-1]
    # @return an integer
    def getMin(self):
        return self.min_values[-1]

if __name__ == "__main__":
    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    print stack.getMin()
    stack.pop()
    print stack.getMin()
