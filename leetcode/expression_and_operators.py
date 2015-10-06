# Given a string that contains only digits 0-9 and a target value, return all 
# possibilities to add binary operators (not unary) +, -, or * between the 
# digits so they evaluate to the target value.
# Time complexity: O(3^n)
# Space complexity: O(3^n)

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def helper(result, sofar, level, value, mult):
            if level == len(num): 
                if value == target: result.append(''.join(sofar))
            else:
                for i in xrange(level, len(num)):
                    if i != level and num[level] == '0': break
                    n = num[level:i + 1]
                    v = int(n)
                    if level == 0:
                        helper(result, sofar + [n], i + 1, v, v)
                    else:
                        helper(result, sofar + ["+", n], i + 1, value + v, v)
                        helper(result, sofar + ["-", n], i + 1, value - v, -v)
                        helper(result, sofar + ["*", n], i + 1, \
                               value - mult + mult * v, mult * v)
            return result
        return helper([], [], 0, 0, 0)
                                                

if __name__ == "__main__":
    solution = Solution()
    print solution.addOperators("123", 6)
    print solution.addOperators("232", 8)
    print solution.addOperators("105", 5)
    print solution.addOperators("00", 0)
    print solution.addOperators("3456237490", 9191)
