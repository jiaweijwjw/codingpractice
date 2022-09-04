# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution():
    def __init__(self) -> None:
        pass

    def find_target(self, nums, target):
        return self._modified_binary_search(nums, target, 0, len(nums)-1, (len(nums)-1)//2)

    def _modified_binary_search(self, nums, target, start, end, mid):
        if start > end:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[start]: # MUST include == condition. mid in left sorted array
            if target > nums[mid] or target < nums[start]: # search right
                start = mid+1
                mid = (start+end)//2
                return self._modified_binary_search(nums, target, start, end, mid)
            else: # search left
                end = mid-1
                mid = (start+end)//2
                return self._modified_binary_search(nums, target, start, end, mid)
        else: # mid in right sorted array
            if target < nums[mid] or target > nums[end]: # search left
                end = mid-1
                mid = (start+end)//2
                return self._modified_binary_search(nums, target, start, end, mid)
            else:
                start = mid+1
                mid = (start+end)//2
                return self._modified_binary_search(nums, target, start, end, mid)


if __name__ == "__main__":
    solution = Solution()
    inputs = [([4,5,6,7,0,1,2],0),([4,5,6,7,0,1,2],3)]
    # outputs: 4, -1
    for nums, target in inputs:
        print(solution.find_target(nums, target))