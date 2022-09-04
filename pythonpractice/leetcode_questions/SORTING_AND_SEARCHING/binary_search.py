# https://leetcode.com/problems/binary-search/
# https://leetcode.com/problems/first-bad-version/

# good explanation of binary search technique:
# https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.

class Solution():
    def __init__(self) -> None:
        pass

    # O(N) space complexity due to recursion stack
    def binary_search(self, arr, start, end, mid, target):
        if start > end:
            return -1 # not found
        if arr[mid] == target:
            return mid # found
        elif arr[mid] > target: # search left
            end = mid-1
            mid = (start+end)//2
            return self.binary_search(arr, start, end, mid, target)
        else: # arr[mid] < target, search right
            start = mid+1
            mid = (start+end)//2
            return self.binary_search(arr, start, end, mid, target)

    # O(1) space complexity
    def binary_search_iterative(self, arr, start, end, mid, target):
        while start <= end: # notice that this includes the equal case
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target: # search left
                end = mid-1
            else:
                start = mid+1
        return -1 # not found

if __name__ == "__main__":
    solution = Solution()
    inputs = [([-1,0,3,5,9,12],9),([-1,0,3,5,9,12],2)]
    # outputs: 4, -1
    for nums, target in inputs:
        print(solution.binary_search(nums, 0, len(nums)-1, (len(nums)-1)//2, target))
        print(solution.binary_search_iterative(nums, 0, len(nums)-1, (len(nums)-1)//2, target))