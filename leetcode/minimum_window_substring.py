# Given a string S and a string T, find the minimum window in S which will 
# contain all the characters in T in complexity O(n).
# Time Complexity: O(n) in average
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        need, begin, end, cur, histogram, remain = {}, 0, len(s), 0, {}, len(t)
        for c in t:
            need[c] = need.get(c, 0) + 1
        for i, c in enumerate(s):
            if c in need:
                histogram[c] = histogram.get(c, 0) + 1
                if histogram[c] <= need[c]: remain -= 1
            while not remain:
                if  i - cur < end - begin: begin, end = cur, i
                if s[cur] in need:
                    histogram[s[cur]] -= 1
                    if histogram[s[cur]] < need[s[cur]]:
                        remain += 1
                cur += 1
        return s[begin:end + 1] if (end - begin) < len(s) else ""

if __name__ == "__main__":
    solution = Solution()
    print solution.minWindow("aa", "aa")
    #print solution.minWindow("ADOBECODEBANC", "ABC")
