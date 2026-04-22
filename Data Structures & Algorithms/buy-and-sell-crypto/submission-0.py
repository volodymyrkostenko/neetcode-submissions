class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while i < len(prices) - 1:
            profit = prices[j] - prices[i]

            max_profit = max(profit, max_profit)

            if j == len(prices) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
                        

        return max_profit 
        