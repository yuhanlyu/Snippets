# Write a function to find the longest common prefix string amongst 
# an array of strings.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        index = 0
        while True:
            for str in strs:
                if index >= len(str) or str[index] != strs[0][index]:
                    return strs[0][:index]
            index += 1
                     
if __name__ == "__main__":
    solution = Solution()
    print solution.longestCommonPrefix(["a", "aa", "aaa", ""])
