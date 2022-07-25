nums = [2, 7, 11, 15]
target = 10

# the original 2 sums can be solved with a dictionary
# what if we can guarantee that the input array is sorted?
# is there a faster way that we can do it?

# the following solution will be using 2 pointers
# it is better than the dict method as it uses O(1) space instead of O(n) space. the time complexity is the same

def find_positions(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        sum = nums[left]+nums[right]
        if sum == target:
            return [left+1, right+1] # the +1 is only because this question wants 1-based indexing
        elif sum > target:
            right -= 1
        else: # sum < target
            left += 1
    return -1 # if number does not exist. but for leetcode, the solution is guaranteed to be found

print(find_positions(nums, target))