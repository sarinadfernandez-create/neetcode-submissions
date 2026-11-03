class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val) #O(n)
        if (self.min and val <= self.min[-1]) or not self.min:
            self.min.append(val)
            #print(self.min)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        #print(self.min)
        self.stack.pop()
        #print(self.min)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# you are only ever popping the last element