# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller 
# elements to the right of nums[i].
# Time Complexity: O(n lg n)
# Space Complexity: O(n)

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            mid = len(enum) / 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                for i in xrange(len(enum) - 1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

if __name__ == "__main__":
    solution = Solution()
    print solution.countSmaller([5, 2, 6, 1])
