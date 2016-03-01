class Solution: 
    
    # @param A: An integer list
    def __init__(self, A):
        self.A = list(A)
        self.B = [0] * len(A)
        for i, num in enumerate(A):
            self.increase(i, num)
    
    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        return self.sum(end) - self.sum(start - 1)

    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        self.increase(index, value - self.A[index])
        self.A[index] = value
            
    def increase(self, index, value):
        while index < len(self.B):
            self.B[index] += value
            index |= index + 1
            
    def sum(self, index):
        sum = 0
        while index >= 0:
            sum += self.B[index]
            index &= index + 1
            index -= 1
        return sum
