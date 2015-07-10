# Given two binary strings, return their sum (also a binary string).
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        c, aindex, bindex = 0, len(a) - 1, len(b) - 1
        result = deque()
        while aindex >= 0 or bindex>= 0 or c:
            if aindex >= 0:
                c += int(a[aindex])
            if bindex >= 0:
                c += int(b[bindex])
            c, reminder = divmod(c, 2)
            result.appendleft(str(reminder))
            aindex -= 1
            bindex -= 1
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print solution.addBinary("11", "1")
