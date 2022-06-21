nums = [4,5,6,7,8,9,0,1,2]
target = 3

# solution2 is the correct answer
# it is simple, just done by modifying original binary search
# note that the hint of O(logn) complexity tells us that it is most likely a binary search solution
# we notice that the array is always split into a left and right sorted array
def solution2(nums, target):
    target_index = binary_search_rotated(nums, target, start=0, end=len(nums)-1, mid=(len(nums)-1)//2)
    return target_index

def binary_search_rotated(nums, target, start, end, mid):
    print(start, end, mid)
    print(nums[start], nums[end], nums[mid])
    print()
    if start > end:
        print("enter")
        return -1
    if nums[mid] == target:
        return mid
    # note that while checking for in left or right sorted array, we include the equal case even though the numbers are distinct
    # if not, we will get stuck when the start, end and mid are at the same pointer
    # we want the recursion to occur even in this case, so as to trigger the start > end to return -1
    if nums[mid] >= nums[start]: # mid is in the left sorted array
        # analyze using the following array: [4,5,6,7,8,9,0,1,2]
        # to come up with the conditions below, analyze the array above and see when do we search left and when to search right
        if target > nums[mid] or target < nums[start]: # search right
            start = mid+1
            mid = (start+end)//2
            return binary_search_rotated(nums, target, start, end, mid)
        else: # search left
            end = mid-1
            mid = (start+end)//2
            return binary_search_rotated(nums, target, start, end, mid)
    elif nums[mid] <= nums[start]: # mid is in the right sorted array
        # analyze using the following array: [7,8,9,0,1,2,3,4,5]
        if target < nums[mid] or target > nums[end]: # search left
            end = mid-1
            mid = (start+end)//2
            return binary_search_rotated(nums, target, start, end, mid)
        else: # search right
            start = mid+1
            mid = (start+end)//2
            return binary_search_rotated(nums, target, start, end, mid)

print(solution2(nums, target))
# the following solution firstly takes up extra space
# secondly, doesnt work for some edge cases
def solution(nums, target):
    target_index = None
    # edge cases
    # check if nums is already sorted / not rotated. note that we cant use sorted() as it is O(nlogn)
    start = 0
    end = len(nums)-1
    mid = end//2
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    if nums[0] < nums[len(nums)-1]: # not rotated
        try:
            target_index = nums.index(target)
        except ValueError as e:
            target_index = -1
            print(e)
    else: # rotated
        rotation_point_index = binary_search_rotation_point(nums, start, end, mid)
        sorted_nums = nums[rotation_point_index:] + nums[:rotation_point_index]
        start = 0
        end = len(sorted_nums)-1
        mid = end // 2
        target_index = binary_search(sorted_nums, target, start, end, mid)
        if target_index != -1:
            target_index += rotation_point_index
    return target_index

# we can think of this as finding the index of the minimum / smallest element in the array
def binary_search_rotation_point(nums, start, end, mid):
    if start > end: # should not enter here as this will not run if the array is already sorted
        return -1
    if nums[mid-1] > nums[mid]:
        return mid
    elif nums[mid] > nums[mid+1]:
        return mid+1
    else:
        if nums[mid] > nums[len(nums)-1]:
            # search right
            start = mid+1
            mid = (start+end)//2
            return binary_search_rotation_point(nums, start, end, mid)
        elif nums[mid] < nums[len(nums)-1]:
            # search left
            end = mid-1
            mid = (start+end)//2
            return binary_search_rotation_point(nums, start, end, mid)
        

def binary_search(sorted_nums, target, start, end, mid):
    if start > end:
        return -1
    if sorted_nums[mid] == target:
        return mid
    elif target > sorted_nums[mid]: # on the right
        start = mid+1
        mid = (start+end)//2
        return binary_search(sorted_nums, target, start, end, mid)
    else: # on the left
        end = mid-1
        mid = (start+end)//2
        return binary_search(sorted_nums, target, start, end, mid)

print(solution(nums, target))
