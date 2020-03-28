'''
Longest String Chain: 
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}  #keep track of words
        longest = 1
        words = sorted(words, key=len) #sort the words by length
        
        for word in words:     #initial length is 1 for all words 
            dp[word] = 1
        
        for word in words:
            for i in range(len(word)):
                if word[:i] + word[i + 1:] in dp:
                    dp[word] = dp[word[:i] + word[i + 1:]] + 1
                    longest = max(longest, dp[word])
        return longest
    
# Complexity Time o(nlogn) = o(nk) where k is the avg length of each word
# Complexity Space o(nk)
   
    
#     Sort the words by word's length. (also can apply bucket sort)
# For each word, loop on all possible previous word with 1 letter missing.
# If we have seen this previous word, update the longest chain for the current word.
# Finally return the longest word chain.