class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.len = 0

    def push(self, val: int) -> None:
        if self.len == 0:
            self.stack.append(val)
            self.minStack.append(val)
            self.len += 1
        else:
            self.minStack.append(min(val, self.minStack[self.len - 1]))
            self.stack.append(val)
            self.len += 1

    def pop(self) -> None:
        if self.len > 0:
            self.stack.pop()
            self.minStack.pop()
            self.len -= 1

    def top(self) -> int:
        return self.stack[self.len - 1]

    def getMin(self) -> int:
        return self.minStack[self.len - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
