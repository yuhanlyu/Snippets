class Solution:
    """
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results
