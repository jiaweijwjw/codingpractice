from math import inf

prices = [7, 1 ,5, 3, 6, 4]

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

# using 2 pointers
def solution(prices):
    left_ptr = 0
    right_ptr = 1
    max_profit = 0
    while right_ptr < len(prices):
        profit = prices[right_ptr] - prices[left_ptr]
        max_profit = max(profit, max_profit) # if the new profit is larger, update it
        if profit < 0: # the left one is not the min
            left_ptr = left_ptr + 1
            right_ptr = right_ptr + 1  
        else:
            right_ptr = right_ptr + 1
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