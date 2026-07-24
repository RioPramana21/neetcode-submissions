class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            sell_price = prices[i]
            if buy_price < sell_price:
                curr_profit = sell_price - buy_price
                max_profit = max(max_profit, curr_profit)
            else:
                buy_price = sell_price

        return max_profit