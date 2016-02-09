class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        def search(k, left, right):
            print nums[left:right + 1], k, left, right
            pivot, begin, end = nums[right], left, right
            while True:
                while nums[left] < pivot and left < right:
                    left += 1
                while nums[right] >= pivot and left < right:
                    right -= 1
                if left >= right:
                    break
                nums[left], nums[right] = nums[right], nums[left]
            nums[left], nums[end] = nums[end], nums[left]
            if k == (left - begin) + 1:
                return nums[left]
            if k < (left - begin) + 1:
                return search(k, begin, left - 1)
            return search(k - (left - begin + 1), left + 1, end)
        return search((len(nums) + 1) / 2, 0, len(nums) - 1)

solution = Solution()
print solution.median([1,2,3,4,5,6,7,100,200,1000])
