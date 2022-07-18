nums = [12, 0, 99999, 8585, 123, 64564, 324523452, 64, 4, 3456246246263, 345]


def binary_search(array_to_be_searched, start, end, target):
    if start > end: return -1
    else:
        mid = start + (end - start)//2
        print(f"mid index: {mid}")
        if target == array_to_be_searched[mid]:
            return mid
        elif target < array_to_be_searched[mid]:
            return binary_search(array_to_be_searched, start, mid-1, target)
        else: # target > mid_val
            return binary_search(array_to_be_searched, mid+1, end, target)

start = 0
end = len(nums)-1
target = int(input("Input a target value that you want to search for: "))
nums.sort() # binary search only works on sorted
print(nums)
found_index = binary_search(nums, start, end, target)
if found_index:
    print(f"target was found at index {found_index}")
else:
    print(f"Target {target} was not found.")

# Geeks for geeks code:

# def binary_search2(arr, l, r, x):
 
#     # Check base case
#     if r >= l:
#         mid = l + (r - l) // 2
#         print(mid)
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, l, mid-1, x)
#         # Else the element can only be present
#         # in right subarray
#         else:
#             return binary_search(arr, mid + 1, r, x)
#     else:
#         # Element is not present in the array
#         return -1