class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, number):
        self.stack.append(number)
        if not self.min_values or number <= self.min_values[-1]:
            self.min_values.append(number)

    def pop(self):
        if self.stack[-1] == self.min_values[-1]:
            self.min_values.pop()
        return self.stack.pop()

    def min(self):
        return self.min_values[-1]
