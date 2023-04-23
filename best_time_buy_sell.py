"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        
        total_profit = 0
        valley = 10000
        peak = valley 

        for i in range(len(prices)-1):

            if (prices[i] < peak):

                total_profit += peak - valley
                valley = prices[i]
                peak = valley

            else :
                peak = prices[i]
        
        total_profit += (peak - valley)
        return total_profit