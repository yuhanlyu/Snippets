# Given a digit string, return all possible letter combinations that the 
# number could represent.
# Time Complexity: O(3^l)
# Space Complexity: O(3^l), l is the length of the input

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []
        map = ["0", "1", "abc", "def", "ghi", "jkl", 
               "mno", "pqrs", "tuv", "wxyz"]
        result = [[]]
        for digit in digits:
            result = [r + [d] for r in result for d in map[int(digit)]]
        return [''.join(item) for item in result]

if __name__ == "__main__":
    solution = Solution()
    print solution.letterCombinations("23")
