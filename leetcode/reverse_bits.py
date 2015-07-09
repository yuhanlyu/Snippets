# Reverse bits of a given 32 bits unsigned integer.
# Time Complexity: O(lg n), n is the number of bits
# Space Complexity: O(1)
# https://graphics.stanford.edu/~seander/bithacks.html#ReverseParallel

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = ((n >> 1) & 0x55555555) | (((n & 0x55555555) << 1) & 0xFFFFFFFF)
        n = ((n >> 2) & 0x33333333) | (((n & 0x33333333) << 2) & 0xFFFFFFFF)
        n = ((n >> 4) & 0x0F0F0F0F) | (((n & 0x0F0F0F0F) << 4) & 0xFFFFFFFF)
        n = ((n >> 8) & 0x00FF00FF) | (((n & 0x00FF00FF) << 8) & 0xFFFFFFFF)
        return (n >> 16) | ((n << 16) & 0xFFFFFFFF)

if __name__ == "__main__":
    solution = Solution()
    print solution.reverseBits(43261596)
