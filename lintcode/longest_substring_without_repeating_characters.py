class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        begin, max_length, last_index = 0, 0, {}
        for index, c in enumerate(s):
            if c in last_index and begin < last_index[c] + 1:
                begin = last_index[c] + 1
            else:
                max_length = max(max_length, index - begin + 1)
            last_index[c] = index
        return max_length
