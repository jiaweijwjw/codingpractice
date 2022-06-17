nums = [2, 7, 11, 15]
target = 18

# this solution is not O(n)
# def find_positions(nums, target):
#     for xindex, x in enumerate(nums):
#         for yindex, y in enumerate(nums[xindex+1:]):
#             if x + y == target:
#                 return [xindex, yindex+xindex+1]

def find_positions(nums, target):
    checked = {}
    for index, num in enumerate(nums):
        rem = target - num
        if rem in checked:
            return [checked[rem], index]
        else:
            checked[num] = index

print(find_positions(nums, target))