from math import inf

class Solution():
    def __init__(self) -> None:
        pass

    # this is the most naive method which is normal recursive / depth first method
    def fewest_coins_to_amount_recursive(self, coins, amount):
        # recursive approach. time limit will exceed
        min_coins_needed = inf
        def recurse(coins, amount, coins_needed):
            nonlocal min_coins_needed
            if amount == 0:
                min_coins_needed = min(min_coins_needed, coins_needed)
            for coin in coins:
                if (amount-coin) >= 0:
                    recurse(coins, amount-coin, coins_needed+1)
        recurse(coins, amount, 0)
        return -1 if min_coins_needed == inf else min_coins_needed

    # the bottom up approach is by first looking at the smaller sub problems then slowly moving our way up to the bigger problems
    # using the results of the smaller problems
    # the top down approach is more natural, similar to how recursion is done. but then we check if the solution to a subproblem
    # has been solved before
    # in my solution for using the top down approach, I used a dictionary. dictionary takes up more space than list but allows for fast access
    # in the bottom down approach, using list has a fast access because the coins needed for an amount can be queried from the list using the amount as the list index

    def fewest_coins_to_amount_bottom_up(self, coins, amount):
        # bottom up DP approach
        coins_needed = [inf]*(amount+1) # use 1 based indexing. cannot initialize to -1 as we checking for min
        coins_needed[0] = 0 # dont forget this line
        for amnt in range(1, amount+1): # range(start, end) end is exclusive
            for coin in coins:
                if amnt >= coin:
                    coins_needed[amnt] = min(coins_needed[amnt], coins_needed[amnt-coin]+1) # either we add this coin or we dont add this coin
        return coins_needed[amount] if coins_needed[amount] != inf else -1


    def fewest_coins_to_amount_top_down(self, coins, amount):
        # top down DP approach
        cache = {} # stores min num of coins needed for a specific amount
        def recurse(amount):
            nonlocal cache
            coins_needed_for_this_amount = inf # for every amount, we need to calculate the coins needed
            if amount == 0: # this is the base case. the recurse function returns values
                return 0
            for coin in coins:
                new_amount = amount - coin
                if new_amount >= 0: # only if this path can be taken. if the coin value is larger than what is left, we cannot use it
                    coins_needed_for_new_amount = cache[new_amount] if new_amount in cache else recurse(new_amount) # calculate the coins needed for the smaller amount (subproblem)
                    # fetch from dict if the value was already calculated. else go calculate it
                    # note that we only save the coins needed for an amount for the main amount, not the subamounts. the subamounts coins needed will be calculated when we enter recursion for that amount
                    coins_needed_for_this_amount = min(coins_needed_for_this_amount, coins_needed_for_new_amount+1) # update if needed
            cache[amount] = coins_needed_for_this_amount # save the coins needed for this specific amount. note that this is done AFTER checking all children (coins)
            return coins_needed_for_this_amount
        min_coins_needed = recurse(amount)
        return min_coins_needed if min_coins_needed != inf else -1



if __name__ == "__main__":
    solution = Solution()
    inputs = [([1,2,5], 11), ([2], 3), ([1], 0)] # 3, -1 , 0
    for coins, amount in inputs:
        # print(solution.fewest_coins_to_amount_bottom_up(coins, amount))
        # print(solution.fewest_coins_to_amount_recursive(coins, amount))
        print(solution.fewest_coins_to_amount_top_down(coins, amount))

# the first idea that comes to find when trying to solve this question would be a greedy solution
# this means that we always go for whatever is the better solution first
# however, we can see that this would have a problem and give incorrect answers.
# for example, consider the case: coins = [1,3,4,5] and amount = 7
# the greedy way would give us 5+1+1 which requires 3 coins. however, 3+4 only requires 2 coins which is lesser

# the next idea that comes to mind would be a depth first solution or recursive solution.
# however, recursive solutions can get exponentially big and would take too long for larger inputs

# to improve recursion, we can use memoization, which is to store the results of previously calculated values
# so that we would not have to recalculate an entire subtree in the recursion tree again
# using memoization with recursion is actually dynamic programming

# when do we know that we can use dynamic programming?
# dp solutions usually works for questions which are optimization problems.
# and what are optimization problems?
# 1. when there are multiple paths to choose from, but we have to choose the best path instead of any path that is a solution
# 2. when we can reuse previous calculations again
# there are many forms for dynamic programming. we dont have to store all the values for it to be calculated as dynamic programming
# kadane's algorithm which stores the previous values is also considered a DP solution

# dynamic programming solutions can be done in 2 main ways. top down and bottom up
# the top down approach is basically recursion + memoization.
# one way to keep track of the already calculated values can be using a dict (to show interviewer), else can use python's LRU_cache
# the top down approach is done in a more natural way as it goes down the recursion tree
# the bottom up approach is when we start from the smaller subproblems and work our way upwards to the bigger problem till the answer we are looking for
# the bottom up approach can use a list instead of a dict since we are starting from ascending numbers in sequence