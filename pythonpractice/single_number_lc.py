from os import remove


nums = [4, 1, 2, 1, 2]

def filter(nums, nums_set):
    for num in nums:
        if num in nums_set:
            nums_set.remove(num)
        else:
            nums_set.add(num)

nums_set = set()
filter(nums, nums_set)
ans = nums_set.pop()
print(ans)