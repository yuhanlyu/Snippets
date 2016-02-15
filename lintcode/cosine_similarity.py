class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        denominator = math.sqrt(sum([x*x for x in A]) * sum([y*y for y in B]))
        if denominator == 0: return 2.0
        return sum([x * y for (x, y) in zip(A, B)]) / denominator
