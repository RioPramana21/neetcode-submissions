class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 101
        for price in prices:
            if price < min_price:
                min_price = price
            new_profit = price - min_price
            if new_profit > profit:
                profit = new_profit
        return profit