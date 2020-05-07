'''
Queue with two stacks 
Implement a queue with two stacks
'''
    def __init__(self):
        self.stackuno = []
        self.stackdos = []
        for i in self.stackuno:
            self.stackdos.append(self.stackuno.pop())
            
    
    def push(self, x: int) -> None:
        self.stackuno.append(x)
        
        
    def pop(self) -> int:
        print(self.stackdos)
        print(self.stackuno)
        if self.stackdos != []:
            return self.stackdos.pop()
        else:
            for i in range(len(self.stackuno)):
                self.stackdos.append(self.stackuno.pop())
                print(self.stackdos)
            return self.stackdos.pop()
            
    def peek(self) -> int:
        if self.stackdos != []:
            return self.stackdos[len(self.stackdos)-1]
        else:
            return self.stackuno[0]
        
    def empty(self) -> bool:
        return self.stackdos == [] and self.stackuno == []
    
    
    