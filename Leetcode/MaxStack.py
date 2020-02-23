'''
Max Stack
Use stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack 
'''

class MaxStack(object): 
    
    def __init__(self):
        self.stack = []
        self.max = []

    def get_max(stack): #returns the largest element in the stack
        elem = 0
        for i in stack:
             if stack[i] > elem:
                 elem = stack[i]
        return elem

