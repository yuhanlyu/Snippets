class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix: return 0
        row, col, count = 0, len(matrix[0]) - 1, 0
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                count, row, col = count + 1, row + 1, col - 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return count
