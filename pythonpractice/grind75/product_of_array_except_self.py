# https://leetcode.com/problems/product-of-array-except-self/

class Solution():
    def __init__(self) -> None:
        pass

    def get_products(self, nums):
        ans = [1]*len(nums)
        prefix = postfix = 1
        for i in range(0, len(nums)-1):
            prefix *= nums[i]
            ans[i+1] *= prefix
        for j in range(len(nums)-1, 0, -1):
            postfix *= nums[j]
            ans[j-1] *= postfix
        return ans


if __name__ == "__main__":
    solution = Solution()
    inputs = [[1,2,3,4],[-1,1,0,-3,3]]
    for nums in inputs:
        print(solution.get_products(nums))