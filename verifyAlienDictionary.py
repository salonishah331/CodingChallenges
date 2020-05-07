'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 
'''



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        
        for i in range(len(order)):
            order_dict[order[i]] = i
            
        for i in range(0, len(words) - 1):
            # compare i and i++
            min_len = min(len(words[i]), len(words[i+1]))
            for k in range(min_len):
                if order_dict[words[i][k]] < order_dict[words[i+1][k]]:
                    break
                elif order_dict[words[i][k]] > order_dict[words[i+1][k]]:
                    return False
                elif k == min_len - 1 and len(words[i]) > len(words[i+1]):
                    return False
                
        return True