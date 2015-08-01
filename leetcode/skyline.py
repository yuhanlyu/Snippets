# Time Complexity: O(n lgn )
# Space Complexity: O(n)

from heapq import heappush, heappop

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        result, heap, i = [], [], 0
        while i < len(buildings) or heap:
            if not heap or i < len(buildings) and buildings[i][0] <= heap[0][1]:
                x = buildings[i][0]
                while i < len(buildings) and buildings[i][0] == x:
                    heappush(heap, (-buildings[i][2], buildings[i][1]))
                    i += 1
            else:
                x = heap[0][1]
                while heap and heap[0][1] <= x:
                    heappop(heap)
            h = -heap[0][0] if heap else 0
            if not result or h != result[-1][1]: result.append([x, h])
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], 
                                [15, 20, 10], [19, 24, 8] ])
