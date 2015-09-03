# Given an array of citations (each citation is a non-negative integer) of a 
# researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index 
# h if h of his/her N papers have at least h citations each, and the other 
# N - h papers have no more than h citations each."
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = [0] * (len(citations) + 1)
        for citation in citations:
            if citation >= len(citations):
                count[len(citations)] += 1
            else:
                count[citation] += 1
        sum = 0
        for i in range(len(citations), -1, -1):
            sum += count[i]
            if sum >= i:
                return i

if __name__ == "__main__":
    solution = Solution()
    print solution.hIndex([3, 0, 6, 1, 5])
