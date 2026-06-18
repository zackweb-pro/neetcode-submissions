class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        max_profit = 0
        for p in prices: 
            min_left = min(p, min_left)
            max_profit = max(max_profit, p-min_left)
        return max_profit