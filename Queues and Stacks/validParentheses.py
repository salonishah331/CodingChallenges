'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''







class Solution:
    def isValid(self,string):
        brackets = {'(' : ')','{' : '}','[' : ']'}
        openers = set(brackets.keys())
        closers = set(brackets.values())

        option = []
        for char in string:
            if char in openers:
                option.append(char)
            elif char in closers:
                if not option: # if the stack it empty it's false
                    return False
                else:
                    if not brackets[option.pop()] == char: # if the closer does not corren
                        return False

        return not option