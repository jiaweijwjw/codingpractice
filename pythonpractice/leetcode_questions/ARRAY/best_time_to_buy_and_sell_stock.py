from math import inf

prices = [7, 1 ,5, 3, 6, 4]

# when we start doing this question, we will first think of it as a very simple question of finding the max and min
# then getting the difference between them
# however, since we only want profits, meaning if the max is before the min, this solution will not work out.
# this simple naive solution is coded out at the end of this script.

# if we dont know what method to use for this, we can try to recall what kind of methods can array questions use.
# this looks like a 2 pointers method to keep track of the min and current.

# using 2 pointers
# the solution is actually very simple
# the base case if there is only 1 price, then no profit will be made so we return profit 0 immediately
# else, we check for the curr profit between left and right
# if there is a negative profit, we know that the new right is the min value, and hence we set the left ptr to that value
# if there is a positive profit, we just move right to check if there is any remaining days that can give a larger profit
# we can just update max_profit only when there is a positive profit and we are required to return 0 if no profit can be made
def solution(prices):
    if len(prices) == 1:
        return 0
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit < 0:
            left = right
            right = left+1
        else:
            max_profit = max(max_profit, profit)
            right += 1
    return max_profit

# using kadane's algorithm if the array given is the profit already, not the prices
def solution2(prices):
    curr_profit = 0
    max_profit = -inf
    for price in prices:
        curr_profit = curr_profit + price
        max_profit = max(curr_profit, max_profit)
        if curr_profit < 0:
            curr_profit = 0 # why does this line work?
    return max_profit


print(solution(prices))
print(solution2(prices))

# following doesnt work as it is just using the very simple idea of finding the max and min
# def solution(prices):
#     profit = 0
#     min_price_index = (None, None) # (price, index)
#     max_price_index = (None, None)
#     for i in range(len(prices)):
#         if min_price_index == (None, None) or prices[i] < min_price_index[0]:
#             min_price_index = (prices[i], i)
#     for j in range(min_price_index[1], len(prices)):
#         if max_price_index == (None, None) or prices[i] > max_price_index[0]:
#             max_price_index = (prices[j], j)
#     profit = max_price_index[1] - min_price_index[1]
#     return profit