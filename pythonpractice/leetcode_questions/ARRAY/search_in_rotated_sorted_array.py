nums = [4,5,6,7,0,1,2]
# nums = [4,5,6,7,8,9,0,1,2]
target = 0


# the question tells us that we have to use an O(logN) algorithm, so we already know that we have to use bianry search
# and also, since it is a sorted array, we know that we can get faster than O(N) searches by using binary search
# the trick to this question is to realize that there is always a right and a left sorted array
# depending on which sorted array the mid value is in, we will have to set our conditions differently
# to check which side mid is, compare mid with the start value. if mid is less than start, mid in is the right sorted array, otherwise mid is in the left sorted array
# to visualize this, draw out the staggered graph of the left and right array
# so what if we know that mid is in the left or the right array?
# notice that if mid is in the left sorted array, target can be on the right of mid if it is larger than mid or less than start
# notice that if mid is in the right sorted array, target can be on the left of mid if it is smaller than mid or greater than end
# lets look at what this means using examples:
# consider the following array: [4,5,6,7,8,9,0,1,2]
# the left sorted array would be from 4 to 9 and the right sorted array would be from 0 to 2
# mid would be 8. notice that mid would only be in the right sorted array if it was less than start which is 4.
# in this case, mid is in the left sorted array
# so how do we determine the condition for the binary search? usually, if target is larger than mid, we search right and if target is less than mid, we search left
# in this case, notice that if target is larger than mid (9) or target is less than start (0,1,2), we search right. else, we search left
# consider the next example array: [7,8,9,0,1,2,3,4,5]
# mid would now be 1. notice that mid is now in the right sorted array. (mid < start) 
# in this case, notice that if target is less than mid (0) or target is larger than end (7,8,9), we search left. else, we search right


class Solution():
    def __init__(self, nums: list) -> None:
        self.nums = nums

    def search_in_rotated_sorted_array(self, target):
        return self._modified_binary_search(self.nums, target, start=0, end=len(self.nums)-1, mid=(len(self.nums)-1)//2)


    def _modified_binary_search(self, arr, target, start, end, mid):
        if start > end: # target not existent in array
            return -1
        if arr[mid] == target: # found
            return mid
        if arr[mid] >= arr[start]: # mid is in the left sorted array
            # consider [4,5,6,7,8,9,0,1,2]
            if target > arr[mid] or target < arr[start]: # search right
                start = mid+1
                mid = (start+end)//2
                return self._modified_binary_search(arr, target, start, end, mid)
            else: # search left
                end = mid-1
                mid = (start+end)//2
                return self._modified_binary_search(arr, target, start, end, mid)
        elif arr[mid] < arr[start]: # mid is in the right sorted array
            # consider [7,8,9,0,1,2,3,4,5]
            if target < arr[mid] or target > arr[end]: # search left
                end = mid-1
                mid = (start+end)//2
                return self._modified_binary_search(arr, target, start, end, mid)
            else: # search right
                start = mid+1
                mid = (start+end)//2
                return self._modified_binary_search(arr, target, start, end, mid)


    def search_in_sorted_array(self, target):
        sorted_array = sorted(self.nums)
        return self._binary_search(sorted_array, target, start=0, end=len(sorted_array)-1, mid=(len(sorted_array)-1)//2)

    # the following is a standard binary search for your reference, the solution to this question is a modified binary search
    # we will return the index of the target if it is found, else we will return -1 if target value cannot be found
    def _binary_search(self, arr, target, start, end, mid):
        if start > end: # target cannot be found
            return -1
        if arr[mid] == target:
            return mid # found!
        elif target > arr[mid]: # target is on the right, search right
            start = mid+1
            mid = (start+end)//2
            return self._binary_search(arr, target, start, end, mid)
        else: # target is on the left, search left
            end = mid-1
            mid = (start+end)//2
            return self._binary_search(arr, target, start, end, mid)

if __name__ == "__main__":
    solution = Solution(nums)
    print(solution.search_in_rotated_sorted_array(0)) # 4
    print(solution.search_in_rotated_sorted_array(1)) # 5
    print(solution.search_in_rotated_sorted_array(6)) # 2
