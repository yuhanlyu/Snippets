# Write a function to return a hint according to the secret number and 
# friend's guess, use A to indicate the bulls and B to indicate the cows. 
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        for i in xrange(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (bulls, both - bulls)

if __name__ == "__main__":
    solution = Solution()
    print solution.getHint("1807", "7810")
    print solution.getHint("1123", "0111")
