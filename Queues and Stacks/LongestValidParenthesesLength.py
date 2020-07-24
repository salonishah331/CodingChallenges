'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''

'''
Instead of finding every possible string and checking its validity, we can make use of stack while scanning the given string to check if the 
string scanned so far is valid, and also the length of the longest valid string. In order to do so, we start by pushing -1−1 onto the stack.

For every \text{‘(’}‘(’ encountered, we push its index onto the stack.

For every \text{‘)’}‘)’ encountered, we pop the topmost element and subtract the current element's index 
from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. 
If while popping the element, the stack becomes empty, we push the current element's index onto the stack. 
In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.

'''




class Solution:
    def longestValidParentheses(self, s: str) -> int:
        parentheses = []
        maxlength = 0 
        parentheses.append(-1)
        
        for i in range(len(s)):
            if s[i] == '(':
                parentheses.append(i)
            else:
                parentheses.pop()
                if not parentheses:
                    parentheses.append(i)
                else:
                    maxlength = max(maxlength, i - parentheses[-1])
        return maxlength



