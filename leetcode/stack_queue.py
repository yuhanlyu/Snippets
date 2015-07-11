# Implement the following operations of a queue using stacks.
# Time Complexity: amortized O(1) for each operation
# Space Complexity: O(n)

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.front = []
        self.end = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.end.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        return self.front.pop()

    # @return an integer
    def peek(self):
        if not self.front:
            while self.end:
                self.front.append(self.end.pop())
        return self.front[-1]

    # @return an boolean
    def empty(self):
        return not self.front and not self.end

if __name__ == "__main__":
    queue = Queue()
    queue.push(0)
    queue.push(1)
    print queue.pop()
    print queue.peek()
    print queue.pop()
    print queue.empty()
