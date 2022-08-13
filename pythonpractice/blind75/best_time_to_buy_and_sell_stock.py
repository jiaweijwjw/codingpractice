# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution():
    def __init__(self) -> None:
        pass

    def get_max_profit(self, stock_prices):
        if len(stock_prices) == 1:
            return 0
        max_profit = 0
        left = 0
        right = 1
        while right < len(stock_prices):
            profit = stock_prices[right] - stock_prices[left]
            if profit < 0:
                left += 1
                right = left + 1 # not just shift right
            else:
                max_profit = max(max_profit, profit)
                right += 1
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    inputs = [[7,1,5,3,6,4],[7,6,4,3,1]]
    # outputs: 5, 0
    for stock_prices in inputs:
        print(solution.get_max_profit(stock_prices))