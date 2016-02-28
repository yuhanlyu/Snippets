class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        solution = [(0, 0)]
        for w, v in sorted(zip(A, V)):
            temp = set(solution)
            for weight, value in solution:
                if w + weight > m:
                    break
                temp.add((w + weight, value - v))
            solution = []
            for item in sorted(temp):
                if not solution or item[1] < solution[-1][1]:
                    solution.append(item)
        return max((-v for w, v in solution))
