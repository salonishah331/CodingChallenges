'''
Max Profit:
    Write an efficient function that takes stock_prices and returns the best profit 
    I could have made from one purchase and one sale of one share of Apple stock yesterday.
    Input: [10, 7, 5, 8, 11, 9]
    Output: 6


    You are given a certain stock's price at different time intervals throughout a day stored in an array. Write an function to determine the maximum profit you can earn that day. You can buy and sell the stock as many times as you want at the array indices.  


'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxProfit = prices[1] - prices[0]
        currmin = prices[0]
        for i in range(len(prices)):
            currprofit =  prices[i] - currmin
            maxProfit = max(currprofit, maxProfit)
            currmin = min(currmin, prices[i])
        return maxProfit
    
    