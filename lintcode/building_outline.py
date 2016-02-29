from heapq import heappush, heappop

class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        result, heap, i = [], [], 0
        buildings.sort()
        while i < len(buildings) or heap:
            if not heap or i < len(buildings) and buildings[i][0] <= heap[0][1]:
                x = buildings[i][0]
                heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            else:
                x = heap[0][1]
                while heap and heap[0][1] <= x:
                    heappop(heap)
            h = -heap[0][0] if heap else 0
            if result and x == result[-1][0] and h > result[-1][-1]:
                result[-1][-1] = h
            elif not result or h != result[-1][-1]:
                if result: result[-1][1] = x
                result.append([x, x, h])
        return [item for item in result if item[-1] != 0]
