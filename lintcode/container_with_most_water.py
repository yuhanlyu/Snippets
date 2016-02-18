class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        result, left, right = 0, 0, len(heights) - 1
        while left < right:
            result = max(result, (right - left) *
                                 min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
