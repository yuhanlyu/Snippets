from math import factorial
class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        result = 1
        for j in range(len(A)):
            result += sum(1 for i in A[j + 1:] if i < A[j]) * factorial(len(A) - j - 1)
        return result

