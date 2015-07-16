# Given an absolute path for a file (Unix-style), simplify it.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        result = []
        for token in (str for str in path.split("/") if str):
            if token == "..":
                if len(result) > 0: result.pop()
            elif token != ".":
                result.append(token)
        return '/' + '/'.join(result)

if __name__ == "__main__":
    solution = Solution()
    print solution.simplifyPath("/home/")
    print solution.simplifyPath("/a/./b/../../c/")
