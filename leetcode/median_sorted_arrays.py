# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity 
# should be O(log (m+n)).
# Time Complexity: O(lg (m + n))
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        def findk(nums1, nums2, K):
            if not nums2: return nums1[K - 1]
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid1 = left + (right - left) / 2 # larger than mid1 numbers
                mid2 = K - mid1 - 1 # need larger than K - mid1 - 1 numbers
                if mid2 >= len(nums2):
                    if mid2 == len(nums2) and nums1[mid1] >= nums2[-1]:
                        return nums1[mid1]
                    left = mid1 + 1
                elif mid2 <= 0:
                    if mid2 == 0 and nums1[mid1] <= nums2[0]:
                        return nums1[mid1]
                    right = mid1 - 1
                elif nums2[mid2 - 1] > nums1[mid1]:
                    left = mid1 + 1
                elif nums2[mid2] < nums1[mid1]:
                    right = mid1 - 1
                elif nums2[mid2 - 1] <= nums1[mid1] <= nums2[mid2]:
                    return nums1[mid1]
                else:
                    return None
        N1, N2 = len(nums1), len(nums2)
        K = (N1 + N2) / 2 + (N1 + N2) % 2
        num1 = findk(nums1, nums2, K)
        if not num1: num1 = findk(nums2, nums1, K)
        if (N1 + N2) % 2: return num1
        num2 = findk(nums1, nums2, K + 1)
        if not num2: num2 = findk(nums2, nums1, K + 1)
        return (num1 + num2) / 2.0
            
if __name__ == "__main__":
    solution = Solution()
    print solution.findMedianSortedArrays([1,1,3,3], [1,1,3,3])
    print solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7], 
                                          [1, 3, 5, 7, 9, 10])
