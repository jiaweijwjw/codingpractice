nums = [2,3,-2,4]

class Solution():
    def __init__(self, nums) -> None:
        self.nums = nums

    def find_maximum_product_subarray(self):
        if len(self.nums) == 1:
            return self.nums[0]
        left = 0
        right = 1
        start, end = 0, 0
        curr_prod = self.nums[left]
        max_prod = self.nums[left]
        while right < len(self.nums):
            prod = curr_prod * self.nums[right]
            if prod < curr_prod:
                # curr_prod = self.nums[right]
                left = right
                right = left+1
                curr_prod = self.nums[left]
            else:
                right += 1
                curr_prod = prod
            if curr_prod > max_prod:
                max_prod = curr_prod
                start = left
                end = right
        print(start, end)
        return max_prod


if __name__ == "__main__":
    solution = Solution(nums)
    print(solution.find_maximum_product_subarray())