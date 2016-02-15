class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        t = s.split()
        return len(t[-1]) if len(t) > 0 else 0
