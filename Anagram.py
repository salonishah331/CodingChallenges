'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''





class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for c in s:
            maps[c] = maps.get(c,0)+1
        for c in t:
            mapt[c] = mapt.get(c,0)+1
        return maps == mapt
        