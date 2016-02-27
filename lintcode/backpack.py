class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        solution = set([0])
        for num in A:
            solution |= set((num + x for x in solution if num + x <= m))
        return max(solution)
