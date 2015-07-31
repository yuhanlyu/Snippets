# Validate if a given string is numeric.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        state, mapping = 0, {"+":2, "-":2, "E":3, "e":3, ".":4, " ":5}
        for c in "0123456789": mapping[c] = 1
        transition = {0:{1:5, 2:3, 5:0, 4:2}, 1:{1:7, 2:4}, 2:{1:6}, 
                      3:{1:5, 4:2}, 4:{1:7}, 5:{1:5, 3:1, 4:6, 5:8}, 
                      6:{1:6, 3:1, 5:8}, 7:{1:7, 5:8}, 8:{5:8}}
        for c in s:
            if c in mapping and mapping[c] in transition[state]:
                state = transition[state][mapping[c]]
            else: return False
        return state >= 5

if __name__ == "__main__":
    solution = Solution()
    print solution.isNumber("0")
    print solution.isNumber(" 0.1 ")
    print solution.isNumber("abc")
    print solution.isNumber("1 a")
    print solution.isNumber("2e10")
