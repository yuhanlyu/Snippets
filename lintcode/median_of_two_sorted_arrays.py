class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        def findk(nums1, nums2, K):
            if not nums2: return nums1[K - 1]
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid1 = left + (right - left) / 2 # larger than mid1 numbers
                mid2 = K - mid1 - 1 # need larger than K - mid1 - 1 numbers
                if mid2 == len(nums2) and nums1[mid1] >= nums2[-1]:
                    return nums1[mid1]
                elif mid2 == 0 and nums1[mid1] <= nums2[0]:
                    return nums1[mid1]
                elif mid2 >= len(nums2):
                    left = mid1 + 1
                elif mid2 <= 0:
                    right = mid1 - 1
                elif nums2[mid2 - 1] > nums1[mid1]:
                    left = mid1 + 1
                elif nums2[mid2] < nums1[mid1]:
                    right = mid1 - 1
                elif nums2[mid2 - 1] <= nums1[mid1] <= nums2[mid2]:
                    return nums1[mid1]
                else:
                    return None
        N1, N2 = len(A), len(B)
        K = (N1 + N2) / 2 + (N1 + N2) % 2
        num1 = findk(A, B, K)
        if not num1: num1 = findk(B, A, K)
        if (N1 + N2) % 2: return num1
        num2 = findk(A, B, K + 1)
        if not num2: num2 = findk(B, A, K + 1)
        return (num1 + num2) / 2.0
