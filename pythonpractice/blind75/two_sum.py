# https://leetcode.com/problems/two-sum/

class Solution():
    def __init__(self) -> None:
        pass

    def get_answer(self, nums, target):
        checked = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in checked:
                return [checked[remainder], i]
            else:
                checked[nums[i]] = i

if __name__ == "__main__":
    solution = Solution()
    inputs = [([2,7,11,15],9),([3,2,4],6),([3,3],6)]
    # outputs: [0,1], [1,2], [0,1]
    for nums, target in inputs:
        print(solution.get_answer(nums, target))
