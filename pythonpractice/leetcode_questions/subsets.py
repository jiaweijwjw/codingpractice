nums = [1, 2, 3]

def solution(nums):
    ans = []
    subset = []
    get_subsets(ans, nums, subset) # start with empty subset
    return ans

def get_subsets(ans, nums, subset):
    print(subset)
    ans.append(subset[:])
    if not nums:
        return
    for i in range(len(nums)):
        subset.append(nums[i])
        # ans.append(subset[:])
        if i == len(nums)-1:
            # return
            get_subsets(ans, [], subset[:]) # after this will enter the not nums condition
            subset.pop(len(subset)-1) # this line is important to pop back out during backtracking
        else:
            get_subsets(ans, nums[i+1:], subset[:])
            subset.pop(len(subset)-1)

def get_subsets2(ans, nums, index, subset):
    ans.append(subset[:])

print(solution(nums))

# another way of doing list.append(element) is list+[element]
# test = [1]
# test = test+[2]
# print(test)