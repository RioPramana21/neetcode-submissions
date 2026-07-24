class MinStack:

    def __init__(self):
        self.stack = []
        self.index = 0
        self.minIndexes = []
        self.min = 0
        self.minIndex = 0

    def push(self, val: int) -> None:
        # self.stack[self.index] = val
        self.stack.append(val)
        if (self.min > val) or (self.index == 0):
            self.min = val
            self.minIndexes.append(self.index)
            self.minIndex += 1
        self.index += 1
        print(self.index)

    def pop(self) -> None:
        del self.stack[(self.index)-1]
        self.index -= 1
        if (self.minIndexes[(self.minIndex)-1] == self.index):
            self.minIndex -= 1
            del self.minIndexes[self.minIndex]
        print(self.stack)

    def top(self) -> int:
        print(self.stack)
        return self.stack[(self.index)-1]

    def getMin(self) -> int:
        print(self.stack)
        return self.stack[self.minIndexes[self.minIndex - 1]]
