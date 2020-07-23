
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''


# dp(i,j) = 1 if Si ... Sj is a palindrome




class Solution:
    def longestPalindrome(self, s: str) -> str:
        solution = ''
        strlen = len(s)
        longestPalLen = 0 
        
        if not s or len(s) == 0:
            return ''
        
        # create 2D array
        dp = [[0 for i in range(strlen)] for j in range(strlen)]
        
        # every letter is a palindrome of itself
        for i in range(strlen):
            dp[i][i] = 1
        solution = s[0:1]
        
        for i in range(strlen -1, -1, -1):
            for j in range(i, strlen, 1):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = 1
                if dp[i][j] and j - i + 1 > len(solution):
                    solution = s[i:j+1]                
                                   
        return solution
             

        
    
      