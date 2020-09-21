'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"


'''



class Solution(object):
    def __init__(self):
        self.lessthan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    # convert last three digits, add "thousands" and convert next three until done
    def numberToWords(self,num):
        if num == 0:
            return "Zero"
        # i = 0 
        words = ""
        for i in range(len(self.thousands)):
            if (num%1000) != 0:
                words = self.helper(num%1000) + self.thousands[i] + " " + words
                # i += 1
            num//= 1000
        return words.strip()
    
    # converts numbers in 100s to words 
    def helper(self, num):
        if (num == 0):
            return ""
        elif (num < 20):
            return self.lessthan20[int(num)] + " "
        elif (num < 100):
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.lessthan20[num // 100] + " Hundred " + self.helper(num % 100)