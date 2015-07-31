# Given n non-negative integers representing the histogram's bar height where 
# the width of each bar is 1, find the area of largest rectangle in the 
# histogram
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack, result = [], 0
        height.append(0)
        for i, h in enumerate(height):
            while stack and h < height[stack[-1]]:
                start = stack[-2] if len(stack) > 1 else -1
                result = max(result, height[stack.pop()] * (i - start - 1))
            stack.append(i)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.largestRectangleArea([2,1,5,6,2,3])
