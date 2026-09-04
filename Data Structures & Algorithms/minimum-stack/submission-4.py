class MinStack:

    def __init__(self):
        self.stack =[]
        self.minimum = []
        

    def push(self, val: int) -> None:
        if len(self.minimum) == 0:
            self.minimum.append(val)
        elif val <= self.minimum[-1]:
            self.minimum.append(val)
        return(self.stack.append(val))
        

    def pop(self) -> None:
        if not self.stack:
            return "Empty Stack"
        v = self.stack.pop()
        if v == self.minimum[-1]:
            self.minimum.pop()
        return v
        

    def top(self) -> int:
        if not self.stack:
            return "Empty Stack"
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
            
                
        
