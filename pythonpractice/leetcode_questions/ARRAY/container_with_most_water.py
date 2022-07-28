from math import inf

nums = [1,8,6,2,5,4,8,3,7]

class Solution():
    def __init__(self, nums) -> None:
        self.nums = nums

    def get_max_volume(self):
        if len(self.nums) == 1: # only got one line, cannot form a container
            return 0
        left = 0
        right = len(self.nums)-1
        max_volume = -inf
        while left < right:
            # adding this 2 conditions should result is slightly faster results? since we can skip some values
            if left > 0 and self.nums[left] <= self.nums[left-1]:
                left += 1
                continue
            elif right < len(self.nums)-1 and self.nums[right] <= self.nums[right+1]:
                right -= 1
                continue
            volume = min(self.nums[left], self.nums[right])*(right-left)
            max_volume = max(max_volume, volume)
            if self.nums[left] < self.nums[right]:
                left += 1
            else:
                right -= 1
        return max_volume
            


if __name__ == "__main__":
    solution = Solution(nums)
    print(solution.get_max_volume())