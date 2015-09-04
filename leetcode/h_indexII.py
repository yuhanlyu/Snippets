# Follow up for H-Index: What if the citations array is sorted in ascending 
# order? Could you optimize your algorithm?
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        low, high = 0, len(citations)
        while low <= high:
            mid = low + (high - low) / 2
            if citations[-mid] >= mid:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

if __name__ == "__main__":
    solution = Solution()
    print solution.hIndex([1, 2, 2, 3, 5])
    print solution.hIndex([0, 1])
    print solution.hIndex([0])
