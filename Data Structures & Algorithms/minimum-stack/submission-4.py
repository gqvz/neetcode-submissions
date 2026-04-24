class MinStack:

    def __init__(self):
        self.s = []
    def push(self, val: int) -> None:
        self.s.append((val, min(val, self.getMin())))
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        if len(self.s) == 0:
            return (2**31-1)
        return self.s[-1][1]
