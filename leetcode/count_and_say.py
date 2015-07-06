# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        result = ['1']
        for _ in xrange(n - 1):
            tmp, count, index = [], 1, 0
            while index < len(result):
                if index == len(result) - 1 or result[index+1] != result[index]:
                    tmp.extend(str(count))
                    tmp.append(result[index])
                    count = 1
                else:
                    count += 1
                index += 1
            result = tmp
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print solution.countAndSay(5)
