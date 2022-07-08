class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = 0,0
        for i in range(len(cost)):  
            curr = min(a, b) + cost[i]
            a, b = curr, a
        return min(a, b)