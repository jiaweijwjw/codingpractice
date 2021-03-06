nums_list = [
    [2,3,-2,4], # 6
    [-2,0,-1], # 0, special case, has 0 and all remaining subarray products are smaller (only happens if single -ve num of left and right side)
    [2,-3,0,1,2], # 2
    [2,3,-2,4,-3] # 144
    ]

# at first look, we may think this solution is similar to the maximum subarray question.
# but for product/multiplication, recall 2 important properties: multiplying a -ve and -ve gives positive. multiplying anything with 0 is 0
# how is this property important?
# notice that for the maximum subarray question, we can just use the current_sum as the current sum is always the maximum up till that point
# however, for multiplication, depending on the signs, the maximum value can be different
# for example, if the current element is a -ve number, when multipled by a positive number, it will become negative
# when multiplied by a negative number, it will become negative
# hence if we only store the previous maximum, we will be taking the current -ve number to multiply a positive number
# to get a new maximum, we will actually have to take the current -ve number to multiply by the previous most -ve number to get a new maximum
# this question is very difficult tbh, dynamic programming questions are general harder to understand
# start by writing the entire process then see what the brute force way is like to notice the pattern
# what is the thing that can be reused in the next iteration?
class Solution():
    def __init__(self, nums) -> None:
        self.nums = nums

    # for this questions, we realise that the we cannot ignore when a number is negative because we have to check whatever is behind also
    # we have to use a global max variable to hold the largest max product that we have seen so far
    # the array will only be broken when there is a 0. we can think of the nums array as between split up by the 0s
    # hence when we see a 0, we restart the entire thing from the next element after the 0
    # if there is a 0, we have to take note of the edge case which is when there is a single negative num before and after it
    def find_maximum_product_subarray(self):
        if len(self.nums) == 1:
            return self.nums[0]
        global_max = self.nums[0]
        curr_min_prod, curr_max_prod = 1, 1 # usually for multiplication, we initialize to 1 as num*1 is num but num*0 is 0
        has_zero = False # this is necessary to handle the edge case
        for num in self.nums:
            if num == 0:
                has_zero = True
                curr_min_prod = 1
                curr_max_prod = 1
                continue
            temp_min = curr_min_prod # required because we need to use min_prod in max_prod again but the value would have been changed
            curr_min_prod = min(num*curr_min_prod, num*curr_max_prod, num)
            curr_max_prod = max(num*temp_min, num*curr_max_prod, num)
            global_max = max(global_max, curr_max_prod)
        if global_max < 0 and has_zero: # [-2,0,-1]
            return 0
        else:
            return global_max

    # if we use the following solution which is the same as maximum_subarray problem,
    # there will be a problem which is once we reach a negative number, we assume that it stops there
    # the trick to solving this is to also store the min_prod together with the max_prod
    # why does this work? 
    # using this example [2,3,-2,4,-3], if we use the same way as maximum_subarray (sum), it will stop at -2
    # however, notice that when -3 is included, it will become positive again
    def find_maximum_product_subarray2(self): # incorrect
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
                end = right-1
        print(start, end)
        return max_prod


if __name__ == "__main__":
    for nums in nums_list:
        solution = Solution(nums)
        print(solution.find_maximum_product_subarray())