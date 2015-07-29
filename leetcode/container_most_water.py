# Given n non-negative integers a1, a2, ..., an, where each represents a point 
# at coordinate (i, ai). n vertical lines are drawn such that the two 
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
# with x-axis forms a container, such that the container contains the most 
# water.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        result, left, right = 0, 0, len(height) - 1
        while left < right:
            result = max(result, (right - left) * 
                                 min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
                

if __name__ == "__main__":
    solution = Solution()
    print solution.maxArea([1, 3, 2])
