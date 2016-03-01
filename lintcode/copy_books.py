class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        def feasible(limit):
            count, sum = 0, 0
            for num in pages:
                if sum + num <= limit:
                    sum += num
                elif num <= limit:
                    count += 1
                    sum = num
                else:
                    return False
            if sum != 0:
                count += 1
            return count <= k
        left, right = 0, 2 ** 31
        while left <= right:
            mid = left + (right - left) / 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
