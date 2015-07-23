# Given a string containing only digits, restore it by returning all possible 
# valid IP address combinations.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        def helper(s, index, level, cur, result):
            if level == 4:
                if index == len(s):
                    result.append('.'.join(cur))
                return
            for i in xrange(1, 4):
                if index + i <= len(s):
                    if (i == 1 or s[index] != '0') \
                    and int(s[index:index + i]) <= 255:
                        cur[level] = s[index:index + i]
                        helper(s, index + i, level + 1, cur, result)
                        cur[level] = ""
            return result
        return helper(s, 0, 0, [""] * 4, [])

if __name__ == "__main__":
    solution = Solution()
    print solution.restoreIpAddresses("25525511135")
    print solution.restoreIpAddresses("010010")
