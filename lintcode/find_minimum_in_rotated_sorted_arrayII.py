class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        left, right = 0, len(num) - 1
        while left < right:
            if num[left] < num[right]: return num[left]
            mid = left + (right - left) / 2
            if num[mid] > max(num[left], num[right]):
                left = mid + 1
            elif num[mid] != num[left]:
                right = mid
            else:
                left += 1
        return num[left]
