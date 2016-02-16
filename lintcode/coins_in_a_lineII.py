class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        if len(values) <= 2: return True
        dp = [0] * (len(values) + 2)
        dp[len(values)-1], dp[len(values)-2] = values[-1], values[-1] + values[-2]
        for i in xrange(len(values) - 3, -1, -1):
            dp[i] = max(values[i] + min(dp[i + 2], dp[i + 3]), 
                        values[i] + values[i+1] + min(dp[i + 4], dp[i + 3]))
        return dp[0] > sum(values) - dp[0]
