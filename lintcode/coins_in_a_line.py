class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        return n % 3 != 0
