# Given a string, find the length of the longest substring without repeating 
# characters. For example, the longest substring without repeating letters 
# for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
# Time Complexity: O(n) in average
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        begin, max_length, last_index = 0, 0, {}
        for index, c in enumerate(s):
            if c in last_index and begin < last_index[c] + 1:
                begin = last_index[c] + 1 
            else:
                max_length = max(max_length, index - begin + 1)
            last_index[c] = index
        return max_length

if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLongestSubstring("abcabcbb")
    print solution.lengthOfLongestSubstring("bbbbb")
