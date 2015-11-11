# Remove the minimum number of invalid parentheses in order to make the input 
# string valid. Return all possible results.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(str):
            count = 0
            for c in str:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0: 
                        return False
            return count == 0
        l = set([s])
        while True:
            valid = filter(isvalid, l)
            if valid:
                return valid
            l = set([x[:i] + x[i+1:] for x in l for i in xrange(len(x))])

if __name__ == "__main__":
    solution = Solution()
    print solution.removeInvalidParentheses("()())()")
    print solution.removeInvalidParentheses("(a)())()")
    print solution.removeInvalidParentheses(")(")
