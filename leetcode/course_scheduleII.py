# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have 
# to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return 
# the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        edges, indegree = [[] for _ in xrange(numCourses)], [0] * numCourses
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        result = deque()
        queue = deque([i for i in xrange(numCourses) if not indegree[i]])
        while queue:
            node = queue.popleft()
            result.appendleft(node)
            for neighbor in edges[node]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]: queue.append(neighbor)
        return list(result) if len(result) == numCourses else []
                
if __name__ == "__main__":
    solution = Solution()
    print solution.findOrder(2, [[1,0]])
    print solution.findOrder(4, [[1,0], [2, 0], [3, 1], [3, 2]])
