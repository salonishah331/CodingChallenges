
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







class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            dp.append(0)
        
        if s == '':
            return 0
        
        for i in range(1,len(s)):
            if s[i] == ')' and s[i-1] == '(' and i :
                dp[i] = dp[i-2] + 2
            if s[i] == ')' and s[i-1] == ')':
                if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1] -2] + 2 
                    
        if s[0] == ')':
            dp[0] = 0
            
        return max(dp)            