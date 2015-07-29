# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it is able to trap after raining.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        h, left, right, result = 0, 0, len(height) - 1, 0
        while left <= right:
            h = max(h, min(height[left], height[right]))
            if height[left] < height[right]:
                if height[left] < h: result += h - height[left]
                left += 1
            else:
                if height[right] < h: result += h - height[right]
                right -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.trap([2, 0, 2])
    print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
