nums = [2, 7, 11, 15]
target = 9

def find_positions(nums, target):
    for xindex, x in enumerate(nums):
        for yindex, y in enumerate(nums[xindex+1:]):
            if x + y == target:
                return [xindex, yindex+xindex+1]

print(find_positions(nums, target))