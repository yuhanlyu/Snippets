# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have 
# to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it 
# possible for you to finish all courses?
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        def cycle(node, edges, visited):
            visited[node] = 1
            for neighbor in edges[node]:
                if visited[neighbor] == 1 or \
                  (visited[neighbor] == 0 
               and cycle(neighbor, edges, visited) == True):
                    return True
            visited[node] = 2
            return False
        edges, visited = [[] for _ in xrange(numCourses)], [0] * numCourses
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])
        for i in xrange(numCourses):
            if visited[i] == 0 and cycle(i, edges, visited) == True:
                return False
        return True
                
if __name__ == "__main__":
    solution = Solution()
    print solution.canFinish(2, [[1,0]])
    print solution.canFinish(2, [[1,0], [0, 1]])
