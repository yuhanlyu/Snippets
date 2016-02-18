class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        A.sort()
        B.sort()
        index1, index2, result = 0, 0, 2 ** 32
        while index1 < len(A) and index2 < len(B):
            if A[index1] <= B[index2]:
                result = min(result, B[index2] - A[index1])
                index1 += 1
                if index1 < len(A) and A[index1] > B[index2]:
                    result = min(result, A[index1] - B[index2])
            else:
                result = min(result, A[index1] - B[index2])
                index2 += 1
                if index2 < len(B) and B[index2] > A[index1]:
                    result = min(result, B[index2] - A[index1])
        return result
