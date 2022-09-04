# https://leetcode.com/problems/binary-search/

class Solution():
    def __init__(self) -> None:
        pass

    def find_target(self, nums, target):
        return self._binary_search(nums, target, 0, len(nums)-1, (len(nums)-1)//2)

    def _binary_search(self, nums, target, start, end, mid):
        if start > end:
            return -1
        if nums[mid] == target:
            return mid
        elif target > nums[mid]: # search right
            start = mid+1
            mid = (start+end)//2
            return self._binary_search(nums, target, start, end, mid)
        else: # search left
            end = mid-1
            mid = (start+end)//2
            return self._binary_search(nums, target, start, end, mid)
        

if __name__ == "__main__":
    solution = Solution()
    inputs = [([-1,0,3,5,9,12],9),([-1,0,3,5,9,12],2)]
    # outputs: 4, -1
    for nums, target in inputs:
        print(solution.find_target(nums, target))