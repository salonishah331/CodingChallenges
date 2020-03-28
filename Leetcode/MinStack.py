'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        """
        initialize your data structure here.
        """
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minstack and self.minstack[-1] >= x:
            self.minstack.append(x)
        elif not self.minstack:
            self.minstack.append(x)
        
    def pop(self) -> None:
        if self.stack and self.stack[-1] == self.minstack[-1]:
            del self.minstack[-1]
        del self.stack[-1]
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(self.minstack)
        if self.minstack:
            return self.minstack[-1]
        else:
            return None
    
    
        
minstack = MinStack()
minstack.push()