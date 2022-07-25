nums = [-1,0,3,5,9,12]
target = 9

class Solution():
    def __init__(self, nums, target) -> None:
        self.nums = nums
        self.target = target
        self.ans = None

    def print_target_index(self):
        print(self.ans)

    def find_target_index(self):
        start = 0
        end = len(self.nums)-1
        mid = end // 2 # use floor division instead of normal division: the / operator
        self.binary_search(self.nums, self.target, start, end, mid)

    def binary_search(self, nums, target, start, end, mid):
        if start > end: # unable to find target
            self.ans = -1
            return
        if nums[mid] == target:
            self.ans = mid
            return
        elif target > nums[mid]: # target is on the right side
            start = mid+1
            mid = (start + end) // 2 # dont forget to use start also because start is not always index 0
            self.binary_search(nums, target, start, end, mid)
        else: # target is on the left side
            end = mid-1
            mid = (start + end) // 2
            self.binary_search(nums, target, start, end, mid)

solution = Solution(nums, target)
solution.find_target_index()
solution.print_target_index()