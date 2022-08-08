# given a sorted array (ascending) consisting of integers including -ve numbers
# find the last negative number (most right negative if any)
# find the first positive number (most left positive if any)

class Solution():
    def __init__(self):
        pass

    def find_last_negative(self, arr, start, end, mid):
        if start > end:
            return -1
        # found
        if mid+1 < len(arr) and arr[mid] < 0 and (arr[mid+1] > 0 or arr[mid+1] == 0):
            return mid
        elif arr[mid] < 0 and mid == len(arr)-1: # if all negative and no positive number
            return mid
        elif arr[mid] < 0:
            # search right
            start = mid+1
            mid = (start+end)//2
            return self.find_last_negative(arr, start, end, mid)
        elif arr[mid] > 0:
            # search left
            end = mid-1
            mid = (start+end)//2
            return self.find_last_negative(arr, start, end, mid)

    def find_first_positive(self, arr, start, end, mid):
        if start > end:
            return -1
        if mid-1 >= 0 and arr[mid] > 0 and (arr[mid-1] < 0 or arr[mid-1] == 0) or mid == 0:
            return mid
        elif arr[mid] > 0 and mid == 0: # if all positive and no negative number
            return mid
        elif arr[mid] < 0:
            # search right
            start = mid+1
            mid = (start+end)//2
            return self.find_first_positive(arr, start, end, mid)
        elif arr[mid] > 0:
            # search left
            end = mid-1
            mid = (start+end)//2
            return self.find_first_positive(arr, start, end, mid)


# basically, the idea is that we do binary search twice. it will still be O(logN) time
# each binary search is to find either the most right negative number or to find the most left positive number
# condition for last negative number would be: the left is negative and the right is not -ve
# condition for first positive number would be: the right is positive and the left is not +ve
# when checking left right, make sure dont go index out of bounds
# edge cases and constraints to consider:
# if there is 0s
# numbers are not unique, there can be multiple 0s also
# all negative numbers
# all positive numbers

if __name__ == "__main__":
    testcases = [[-10,-5,-1,1,4,6,10,100], [], [-10,-8,-3], [2,3,4]]
    # [2,3], [-1,-1], [2, -1], [-1, 0]
    for arr in testcases:
        solution = Solution()
        last_neg = solution.find_last_negative(arr, 0, len(arr)-1, (len(arr)-1)//2)
        first_pos = solution.find_first_positive(arr, 0, len(arr)-1, (len(arr)-1)//2)
        print([last_neg, first_pos])