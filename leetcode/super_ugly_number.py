# Write a program to find the nth super ugly number.
# Super ugly numbers are positive numbers whose all prime factors are in the 
# given prime list primes of size k.
# Time Complexity: O(n lg n)
# Space Complexity: O(n)

import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]: 
                uglies.append(ugly)
        return uglies[-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.nthSuperUglyNumber(12, [2, 7, 13, 19])
