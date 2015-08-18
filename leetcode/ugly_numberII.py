# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 
# ugly numbers.
# Note that 1 is typically treated as an ugly number.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        numbers, indices, factors = [1], [0, 0, 0], [2, 3, 5]
        for i in xrange(n - 1):
            next = min([numbers[indices[j]] * factors[j] for j in xrange(3)])
            numbers.append(next)
            indices[:] = [indices[j] + 
                          (1 if numbers[indices[j]] * factors[j] == next else 0)
                          for j in xrange(3)]
        return numbers[-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.nthUglyNumber(10)
