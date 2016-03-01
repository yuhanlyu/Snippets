class Solution: 
    
    # @param A: An integer list
    def __init__(self, A):
        self.nums, self.tree = [0] * len(A), [0] * len(A)
        for i, num in enumerate(A):
            self.modify(i, num)

    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        return self.sum(end) - self.sum(start - 1)

    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        d, self.nums[index] = value - self.nums[index], value
        while index < len(self.nums):
            self.tree[index] += d
            index |= index + 1
            
    def sum(self, index):
        ans = 0
        while index >= 0:
            ans += self.tree[index]
            index = (index & (index + 1)) - 1
        return ans
