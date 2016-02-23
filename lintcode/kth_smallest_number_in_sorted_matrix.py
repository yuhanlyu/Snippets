import heapq
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        indices, pq = [0] * len(matrix), []
        for i in xrange(len(indices)):
            heapq.heappush(pq, (matrix[i][0], i))
        for _ in xrange(k - 1):
            n, i = heapq.heappop(pq)
            if indices[i] < len(matrix[i]) - 1:
                indices[i] += 1
                heapq.heappush(pq, (matrix[i][indices[i]], i))
        return heapq.heappop(pq)[0]
