# You are playing the following Nim Game with your friend: There is a heap of 
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. 
# You will take the first turn to remove the stones.
# Both of you are very clever and have optimal strategies for the game. 
# Write a function to determine whether you can win the game given the number 
# of stones in the heap.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & 3 > 0
                                        

if __name__ == "__main__":
    solution = Solution()
    print solution.canWinNim(4)
    print solution.canWinNim(5)
