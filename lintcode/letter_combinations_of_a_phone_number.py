class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        if not digits: return []
        map = ["0", "1", "abc", "def", "ghi", "jkl",
               "mno", "pqrs", "tuv", "wxyz"]
        result = [[]]
        for digit in digits:
            result = [r + [d] for r in result for d in map[int(digit)]]
        return [''.join(item) for item in result]
