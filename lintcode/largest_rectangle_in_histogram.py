class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        stack, result = [], 0
        height.append(0)
        for i in xrange(len(height)):
            j = i - 1
            while j >= 0 and height[j] > height[i]:
                result = max(result, height[j] * (i - j))
                height[j], j = height[i], j - 1
        return result
