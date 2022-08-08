from math import inf
class Solution():
    def __init__(self) -> None:
        pass

    def fewest_coins_to_amount(self, coins, amount):
        # bottom up DP approach
        coins_needed = [inf]*(amount+1) # use 1 based indexing. cannot initialize to -1 as we checking for min
        coins_needed[0] = 0 # dont forget this line
        for amnt in range(1, amount+1): # range(start, end) end is exclusive
            for coin in coins:
                if amnt >= coin:
                    coins_needed[amnt] = min(coins_needed[amnt], coins_needed[amnt-coin]+1) # either we add this coin or we dont add this coin
        return coins_needed[amount] if coins_needed[amount] != inf else -1


if __name__ == "__main__":
    solution = Solution()
    coins = [1,2,5]
    amount = 11
    print(solution.fewest_coins_to_amount(coins, amount))