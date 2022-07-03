num_arr = [-2,1,-3,4,-1,2,1,-5,4] # answer should be 6
# num_arr = [-3, 2, -5, 1, 1, 1]
# num_arr = [1, -2]
# num_arr = [-2, 1]


# we will start from the first 2 item, using left and right ptr
# the idea is that if the sum = curr_sum + new number is less than the curr sum, we can ignore everything in front
# we do this by setting left to the right
# else, we will continue expand the window by only shifting the right pointer
# the benefit of this 2 pointers is that we can also return the index of the start and end of the max subarray
def solution(nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = 1
    start, end = 0, 0 # index for the start and end of maximum subarray
    # init
    curr_sum = nums[left]
    max_sum = nums[left]
    while right < len(nums):
        sum = curr_sum + nums[right]
        if sum < nums[right]: # extend both left and right, ignoring everything on the left
            curr_sum = nums[right]
            left = right
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

if __name__ == "__main__":
    print(solution(num_arr))    


# comments:
# ends at this number, or start a new one
# -ve + -ve will become more -ve which is smaller
# either the prev sum of the new sum which includes the current number
# if the new sum is larger than the global max, change the global max
# what if we want to keep track of the indexes?

# KADANE's
# to solve this problem, we can use the kadane's algorithm
# basically the idea is that firstly, we want to find what is the largest subarray ending at a particular index / element
# kadane's algorithm allows us to traverse the array once O(n) and for each index, the largest subarray is either:
# the current element or the subarray of the current element + the prev largest subarray