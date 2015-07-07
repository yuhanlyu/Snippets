# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C - A) * (D - B) + (G - E) * (H - F)
        overlap_width = max(min(C, G) - max(A, E), 0)
        overlap_height = max(min(D, H) - max(B, F), 0)
        return area - overlap_width * overlap_height
                                            

if __name__ == "__main__":
    solution = Solution()
    print solution.computeArea(-2, -2, 2, 2, -1, 4, 1, 6)
