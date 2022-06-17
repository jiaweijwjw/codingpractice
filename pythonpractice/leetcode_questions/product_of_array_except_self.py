nums = [1, 2, 3, 4]
# ans: [24, 12, 8, 6]

# using prefix and postfix arrays
# basically what we do is we go through the array once from left to right to fill the prefix array
# and for each element, we calculate the prefix till that element (inclusive) and store it in prefix array
# then we go through the array once from right to left to fill the postfix array
# and for each element, we calculate the postfix from that element (inclusive) and store it in postfix array
# the idea is that each time the pointer moves left or right (depending on which pass),
# the pre or postfix till that element makes use of the previous position of the pointer (arr[ptr])
# prefix = [1, 2, 6, 24]
# postfix = [24, 24, 12, 4]
def solution(nums):
    ans = [1] * len(nums) # we have to do this because we have to multiple the prev postfix/prefix for the first and last element
    # also, we have to initialize the ans array cos we will be access the indexes in it
    prefix, postfix = ans[:], ans[:]
    for index, num in enumerate(nums): # left to right pass
        if index == 0: # first element
            prefix[index] = num
        else:
            prefix[index] = prefix[index-1]*num
    for index, num in reversed(list(enumerate(nums))): # right to left pass
        if index == len(nums)-1: # last element
            postfix[index] = num
        else:
            postfix[index] = postfix[index+1]*num
    # now we will fill up the ans array
    # basically what we are doing is that for each index j
    # we calculate ans[j] as prefix[j-1]*postfix[j+1] aka prefix of the index before and postfix of the index after this element
    for i in range(len(nums)):
        if i == 0:
            ans[i] = postfix[i+1]
        elif i == len(nums)-1:
            ans[i] = prefix[i-1]
        else:
            ans[i] = prefix[i-1]*postfix[i+1]
    return ans

# the above solution is almost there but we are using extra space to store the prefix and postfix
# so further optimize, we can actually just do the same thing, do the pass from left to right for prefix
# but instead of storing it in a prefix array, we just store it in the ans array
# then we will continue to do the pass from right to left for postfix and since the prefix for a particular position is already in ans array,
# we just multiple the postfix value into whatever value is already in ans[index]
# however to make this work, one small change that we would have to make is that when we are storing prefix,
# we store it in the next position on the right for ans
# and when we are storing postfix, we store it in the prev position on the left for ans
def solution2(nums):
    ans = [1]*len(nums)
    prefix = 1
    postfix = 1
    for i in range(0, len(nums)-1): # first element till second last element, left to right
        prefix = prefix*nums[i]
        ans[i+1] = prefix
    for j in range(len(nums)-1, 0, -1): # last element till second element, right to left
        postfix = postfix*nums[j]
        ans[j-1] = ans[j-1]*postfix
    return ans

# additional note: range end in not inclusive!! the following code shows the printing of the nums array 
# for i in range(0, len(nums)-1):
#     print(nums[i])
# for j in range(len(nums)-1, 0, -1):
#     print(nums[j])
# for x in range(len(nums)):
#     print(nums[x])

print(solution(nums))
print(solution2(nums))