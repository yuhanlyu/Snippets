class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        h, left, right, result = 0, 0, len(heights) - 1, 0
        while left <= right:
            h = max(h, min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                if heights[left] < h: result += h - heights[left]
                left += 1
            else:
                if heights[right] < h: result += h - heights[right]
                right -= 1
        return result
