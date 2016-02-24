class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        self.stack2.append(element)

    def top(self):
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1[-1]

    def pop(self):
        self.top()
        return self.stack1.pop()
