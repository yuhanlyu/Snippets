# Count the number of prime numbers less than a non-negative number, n.
# Time Complexity: O(n lg lg n)
# Space Complexity: O(n)

import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime, count = [True] * (n), n - 2 if n > 2 else 0
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in xrange(i * i, n, i):
                    if isPrime[j]:
                        count -= 1
                        isPrime[j] = False
        return count

if __name__ == "__main__":
    solution = Solution()
    print solution.countPrimes(100)
