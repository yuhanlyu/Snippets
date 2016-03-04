import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if sum([1 for num in nums if num > 0]) <= k:
            return sum(heapq.nlargest(k, nums))

        P, stack, profits = self.normalize(nums), [], []
        for i in xrange(0, len(P) / 2):
            l, h = P[2 * i], P[2 * i + 1]
            while stack and stack[-1][0] >= l:
                lt, ht = stack.pop()
                profits.append(ht - lt)
            while stack and stack[-1][1] <= h:
                if stack[-1][1] - l > 0:
                    profits.append(stack[-1][1] - l)
                (l, _) = stack.pop()
            stack.append((l, h))
        while stack:
            profits.append(stack[-1][1] - stack[-1][0])
            stack.pop()
        return sum(heapq.nlargest(k, profits))

    def normalize(self, nums):
        nums = [num for num in nums if num != 0]
        for i in xrange(len(nums)):
            if nums[i] > 0:
                nums = nums[i:]
                break
        for i in xrange(len(nums), 0, -1):
            if nums[i - 1] > 0:
                nums = nums[:i]
                break
        P, end = [0], 0
        while True:
            cur = 0
            while end < len(nums) and nums[end] > 0:
                cur += nums[end]
                end += 1
            P.append(P[-1] + cur)
            if end == len(nums):
                break
            cur = 0
            while nums[end] < 0:
                cur += nums[end]
                end += 1
            P.append(P[-1] + cur)
        return P

solution = Solution()
print solution.maxSubArray([-1,4,-2,3,-2,3], 2)
