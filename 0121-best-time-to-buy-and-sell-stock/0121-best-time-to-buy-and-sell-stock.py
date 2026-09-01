class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = -1

        for i in range(len(prices)):
            if(prices[i] < buy):
                buy = prices[i]
            else:
                profit = prices[i] - buy
                max_profit = max(profit, max_profit)
        return max_profit
            