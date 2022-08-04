from math import inf

class Solution():
    def __init__(self) -> None:
        pass

    def get_max_area(self, nums):
        # edge cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        left = right = len(nums)//2
        max_area = -inf
        min_height = inf
        while left >= 0 and right <= len(nums)-1:
            min_height = min(min_height, nums[left], nums[right])
            area = min_height*(right-left+1)
            max_area = max(max_area, area, nums[left], nums[right])
            if nums[left] < nums[right]:
                left -= 1
            else:
                right += 1
        return max_area

if __name__ == "__main__":
    inputs = [[7,3,4,6,2], [1,3,2,6,5,1], [8,2,1,4,1], [15,1,2,4,1,7,3,5,2,6,1,10,1,2,3,4,0,8], [], [8]]
    solution = Solution()
    for nums in inputs:
        print(solution.get_max_area(nums))
    