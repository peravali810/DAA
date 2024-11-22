class MinStack:

    def __init__(self):
        self.stak=[]
        self.minstak=[]

    def push(self, val: int) -> None:
        self.stak.append(val)
        if not self.minstak or val<=self.minstak[-1]:
            self.minstak.append(val)

    def pop(self) -> None:
        if self.stak.pop() == self.minstak[-1]:
            self.minstak.pop()

    def top(self) -> int:
        return self.stak[-1]

    def getMin(self) -> int:
        return self.minstak[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()