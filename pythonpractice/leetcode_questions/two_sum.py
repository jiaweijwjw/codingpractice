nums = [2, 7, 11, 15]
target = 18

# this solution is not O(n)
# def find_positions(nums, target):
#     for xindex, x in enumerate(nums):
#         for yindex, y in enumerate(nums[xindex+1:]):
#             if x + y == target:
#                 return [xindex, yindex+xindex+1]

# the idea for this question is that we go through each element and store them into the checked dict
# note that we store the value as the key and the index as the value as we are required to return the index of answers
# for every iteration, we will check if there is any value in checked that sums up to target when added with the curr value
def find_positions(nums, target):
    checked = {}
    for index, num in enumerate(nums):
        rem = target - num
        if rem in checked:
            return [checked[rem], index]
        else:
            checked[num] = index

print(find_positions(nums, target))