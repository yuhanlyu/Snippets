# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. Except for 
# the first two numbers, each subsequent number in the sequence must be the 
# sum of the preceding two.
# Time Complexity: O(n^3)
# Space Complexity: O(n)

class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(1, len(num) - 1):
            first = num[:i]
            if first != str(int(first)):
                continue
            for j in xrange(i + 1, len(num)):
                second = num[i:j]
                if second != str(int(second)):
                    continue
                a, b, k = first, second, j
                while k < len(num):
                    next = str(int(a) + int(b))
                    if not num.startswith(next, k):
                        break
                    k, a, b = k + len(next), b, next
                if k == len(num):
                    return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.isAdditiveNumber("112358")
    print solution.isAdditiveNumber("199100199")
    print solution.isAdditiveNumber("1203")
    print solution.isAdditiveNumber("111122335588143")
