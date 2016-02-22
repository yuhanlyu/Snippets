class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        result = []
        for token in (str for str in path.split("/") if str):
            if token == "..":
                if len(result) > 0: result.pop()
            elif token != ".":
                result.append(token)
        return '/' + '/'.join(result)
