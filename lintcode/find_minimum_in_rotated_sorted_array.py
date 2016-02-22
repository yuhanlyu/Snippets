class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] <= num[right]: return num[left]
            mid = left + (right - left) / 2
            if num[left] <= num[mid]:
                left = mid + 1
            else:
                right = mid
