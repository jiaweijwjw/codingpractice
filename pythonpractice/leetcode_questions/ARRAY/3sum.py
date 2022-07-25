# this question can be done with the knowledge of two_sum and two_sum2
# to recall the difference between two_sum and two_sum2, for two_sum2, the input array is sorted
# both two_sum and two_sum2 can be solved using the dictionary method by with the sorted input, two_sum2 can be solved with 2 pointers too
# how do we break down this problem into a two_sum problem?
# we can iterate through the nums array and set target as 0 - the current num
# then for the remaining array behind, it will become a two_sum problem by trying to find 2 numbers that sum up to this target
# the first problem that we can think about is that if we use the two_sum dictionary method, for each iteration, we will need to create a dict
# this is not very efficient in terms of space complexity
# so can we sort the array and make it the two_sum2 problem? yes we can! then we can use the 2 pointer method
# also, by sorting the nums array, we will also be able to fulfil the requirement that the solution set does not contain duplicate triplets
# this can be easily done by skipping an iteration if it is the same as the number in the previous iteration
# the 2 pointer method will be slightly different compared to the original two_sum2
# firstly, there may be different pairs that sum up to the same target, so we will have to continue checking even after we found a valid pair
# this was not needed as two_sum2 guaranteed one solution
# note that when we continue checking for more valid pairs, we CANNOT move both left and right inwards after a valid pair as some cases may be missed
# also, the duplicate triplet condition must also be handled in this part, using the same method as the outer loop

# nums = [-1,0,1,2,-1,-4]
nums = [-2,-2,0,0,2,2]

def find_triplets(nums):
    ans_triplets = []    
    if len(nums) < 3:
        return ans_triplets
    nums.sort()
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i-1]: # skip this iteration if its repeated
            continue
        target = 0-nums[i]
        # from here its just two_sums2
        left, right = i+1, len(nums)-1
        left_bound, right_bound = left, right
        while left < right:
            if left > left_bound and nums[left] == nums[left-1]:
                left += 1
                continue
            elif right < right_bound and nums[right] == nums[right+1]:
                right -= 1
                continue
            sum = nums[left]+nums[right]
            if sum == target:
                ans_triplets.append([nums[i], nums[left], nums[right]])
                left += 1 # just move either left or right inwards
                # shifting both left and right inwards may also miss some case
                # break / continue doesnt work as there may be more solutions
            elif sum > target:
                right -= 1
            else: # sum < target
                left += 1
    return ans_triplets

print(find_triplets(nums))