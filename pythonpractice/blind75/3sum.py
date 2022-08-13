# https://leetcode.com/problems/3sum/

class Solution():
    def __init__(self) -> None:
        pass

    def get_triplets(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                elif right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                sum = nums[left] + nums[right]
                if sum == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    inputs = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    # outputs: [[-1,-1,2],[-1,0,1]], [], []
    for nums in inputs:
        print(solution.get_triplets(nums))