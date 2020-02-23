''' 
Bracket Validator
Write a function to determine whether the openers and closers are properly nested 
Input: '{[]()}'
Output: True
'''
def BracketValidator(string):
    stack = []
    for i in string: 
        if string[i] == '{' or '[' or '(': 
            stack.append(string[i])
        elif 