class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        if len(prices) in [0, 1]:
            return 0
        
        
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
        return max_profit
                
        