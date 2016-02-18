class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        index = 0
        while True:
            for str in strs:
                if index >= len(str) or str[index] != strs[0][index]:
                    return strs[0][:index]
            index += 1
