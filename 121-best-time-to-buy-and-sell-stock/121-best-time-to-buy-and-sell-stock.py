class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            sell = price
            profit_1 = sell-buy
            if profit_1<0:
                sell = 0
                profit_1 = 0
            if buy>sell:
                buy = price
            profit = max(profit, profit_1)
        return profit
            
                
        