class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # check if the length of prices is 0 or 1
        if len(prices) in [0, 1]:
            return 0
      
        # left, right pointer method
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1
            
        return max_profit 
      
        
        # more memory efficient solution
#        max_profit = 0
#        min_price = prices[0]
        
#        for price in prices:
#            if price - min_price > max_profit:
#                max_profit = price - min_price
#            if price < min_price:
#                min_price = price
#        return max_profit
                
        