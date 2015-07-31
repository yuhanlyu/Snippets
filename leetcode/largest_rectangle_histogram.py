# Given n non-negative integers representing the histogram's bar height where 
# the width of each bar is 1, find the area of largest rectangle in the 
# histogram
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack, result = [], 0
        height.append(0)
        for i in xrange(len(height)):
            j = i - 1
            while j >= 0 and height[j] > height[i]:
                result = max(result, height[j] * (i - j))
                height[j], j = height[i], j - 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.largestRectangleArea([2,1,5,6,2,3])
