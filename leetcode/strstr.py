# Returns the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if needle == "": 
            return 0
        failure = [-1] * (len(needle) + 1)
        for index in xrange(1, len(needle) + 1):
            pos = failure[index - 1]
            while pos != -1 and needle[pos] != needle[index - 1]:
                pos = failure[pos]
            failure[index] = pos + 1
        ti, pi = 0, 0
        for ti in xrange(len(haystack)):
            while pi != -1 and haystack[ti] != needle[pi]:
                pi = failure[pi]
            pi += 1
            if pi == len(needle):
                return ti + 1 - len(needle)
        return -1

if __name__ == "__main__":
    solution = Solution()
    print solution.strStr("", "")
    print solution.strStr("abbccde", "ccdcc")
    print solution.strStr("abbccde", "ef")
