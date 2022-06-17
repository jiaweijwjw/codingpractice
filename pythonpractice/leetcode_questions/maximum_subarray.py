# to solve this problem, we can use the kadane's algorithm
# basically the idea is that firstly, we want to find what is the largest subarray ending at a particular index / element
# kadane's algorithm allows us to traverse the array once O(n) and for each index, the largest subarray is either:
# the current element or the subarray of the current element + the prev largest subarray

from math import inf

num_arr = [-2,1,-3,4,-1,2,1,-5,4] # answer should be 6
# num_arr = [1,-3,5,2]
# num_arr = [-5, -3, -1, -2]
# counter: 4
# start_index: 3
# end_index: 6
# ans: 6

# def solution(num_arr):
#     counter = 1 # keep track length of the largest subarray
#     current_sum = 0 # keeps track of current sum of subarray ending with this element
#     max_sum = -inf # keep track max sum of the largest subarray
#     start_index = 0 # keep track the start and end index of the largest subarray
#     for index, num in enumerate(num_arr):
#         sum = current_sum + num
#         current_sum = max(sum , num)
#         max_sum = max(max_sum, current_sum)
#     # return (counter, start_index, start_index+counter, max_sum)
#     return max_sum
        
# def solution(num_arr):
#     counter = 1
#     curr_sum = 0
#     global_max_sum = -inf
#     start_index = 0
#     for index, num in enumerate(num_arr):
#         new_sum = curr_sum + num
#         if new_sum  < curr_sum: # adding this new number makes the sum smaller

# geekforgeeks code:
def solution(num_arr):
    max_so_far = -inf
    max_ending_here = 0
    for num in num_arr:
        max_ending_here = max_ending_here + num
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(solution(num_arr))

# ends at this number, or start a new one
# -ve + -ve will become more -ve which is smaller
# either the prev sum of the new sum which includes the current number
# if the new sum is larger than the global max, change the global max
# what if we want to keep track of the indexes?
