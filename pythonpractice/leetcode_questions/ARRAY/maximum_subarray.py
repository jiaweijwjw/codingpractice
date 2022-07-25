from math import inf
num_arr = [-2,1,-3,4,-1,2,1,-5,4] # answer should be 6
# num_arr = [-3, 2, -5, 1, 1, 1]
# num_arr = [1, -2]
# num_arr = [-2, 1]

# this is an array question, and since we are looking at subarrays which are contiguous, we can think of the sliding window technique or the 2 pointer technique
# this question is actually not easy. have to draw out each pattern by hand so observe first
# most solutions provided on leetcode will just use kadane's algorithm.
# but i came up with a 2 pointers x sliding windows method which is easier to understand and hence easier to remember, rather than memorizing the kadane's algorithm
# since this method is similar is time complexity as using kadane's
# also, this method can return the index of the max subarray as compare to kadane's which only returns the largest sum of the subarray

# we will start from the first 2 item, using left and right ptr
# the trick/idea is that if the sum = curr_sum + new number is less than the curr sum, we can ignore everything in front
# this trick/idea can only be realised if you write down the entire process by hand and analyze the pattern
# if cannot understand the pattern, can go watch youtube for explanation then come back here
# we do this by setting left to the right
# else, we will continue expand the window by only shifting the right pointer
# the benefit of this 2 pointers is that we can also return the index of the start and end of the max subarray
def solution(nums):
    if len(nums) == 1: # base case
        return nums[0]
    left = 0
    right = 1 # since we already accounted for the base case, we can assume that the array size is >= 2 so we can start right at index 1
    start, end = 0, 0 # index for the start and end of maximum subarray
    # init
    curr_sum = nums[left]
    max_sum = nums[left]
    while right < len(nums):
        sum = curr_sum + nums[right]
        if sum < nums[right]: # extend both left and right, ignoring everything on the left
            curr_sum = nums[right]
            left = right # ignore everything on the left
            right = left+1
        else: # extend right
            curr_sum = sum
            right += 1
        if curr_sum > max_sum:
            max_sum = curr_sum
            start, end = left, right-1 # right is always ahead by 1 beacuse we incremented the pointers before checking for max
    print(start, end)
    return max_sum
# pseudo code
# first if nums only has a single element, that is the longest subarray, so we can return / exit early
# also, this is because we are using 2 pointers, whereby the left and right starts at index 0 and 1 respectively
# we have to make sure right ptr is not out of index, so the len of nums must be at least 2
# then we do the initialization of the variables that we are going to use
# left and right is to keep track of the current subarray which we will be looking at
# start and end is to keep track of the start and end index of the largest sum subarray
# curr_sum and max_sum will be set to the first element initially
# then we start to move the 2 pointers. if the curr_sum + current number that right is pointing at gives a sum that is less than the current number,
# we know that the current number itself is already larger than the subarray directly connecting to it.
# hence we can ignore the previous stuff and move the left pointer. 
# moving the left pointer is like "resetting" the subarray


# this solution is slightly faster than the above
# using kadane's algorithm
def solution2(nums):
    if len(nums) == 1:
        return nums[0]
    max_sum = -inf
    curr_sum = 0
    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    print(solution2(num_arr))    


# KADANE's SIMPLE EXPLANATION, or go watch youtube
# to solve this problem, we can use the kadane's algorithm
# basically the idea is that firstly, we want to find what is the largest subarray ending at a particular index / element
# kadane's algorithm allows us to traverse the array once O(n) and for each index, the largest subarray is either:
# the current element or the subarray of the current element + the prev largest subarray