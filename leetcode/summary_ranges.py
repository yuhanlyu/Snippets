# Given a sorted integer array without duplicates, 
# return the summary of its ranges.
# Time Complexity: O(n)
# Space Complexity: O(output)

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        def range_to_string(begin, end):
            return str(begin)+ "->" + str(end) if begin != end else str(begin)
        if not nums:
            return []
        result, begin = [], 0
        for index in xrange(1, len(nums)):
            if nums[index] > nums[index - 1] + 1:
                result.append(range_to_string(nums[begin], nums[index-1]))
                begin = index
        result.append(range_to_string(nums[begin], nums[-1]))
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.summaryRanges([0])
