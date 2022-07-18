class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) in [0, 1]:
            return 0
        
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
            
                
        