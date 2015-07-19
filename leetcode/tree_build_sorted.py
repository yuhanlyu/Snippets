# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        def helper(nums, begin, end):
            if begin == end: return None
            mid = begin + (end - begin) / 2
            root = TreeNode(nums[mid])
            root.left, root.right = helper(nums, begin, mid), \
                                    helper(nums, mid + 1, end)
            return root
        return helper(nums, 0, len(nums))

if __name__ == "__main__":
    solution = Solution()
    node = solution.sortedArrayToBST([1, 2, 3])
    print node.val, node.left.val, node.right.val
