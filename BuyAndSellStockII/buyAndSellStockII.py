def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        current_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if profit < 0 or profit < current_profit:
                total_profit += current_profit
                current_profit = 0
                buy = prices[i]
            else:
                current_profit = max(profit, current_profit)
                # print('current_profit', current_profit)
        total_profit += current_profit
        return total_profit
