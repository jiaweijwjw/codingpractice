# swapping 2 values in a list
# nums = [x for x in range(1, 7)]
# print(nums)
def swap(a, b, mylist):
    mylist[a], mylist[b] = mylist[b], mylist[a]

# def swap2(a, b, mylist):
#     tmp = mylist[a]
#     mylist[a] = mylist[b]
#     mylist[b] = tmp

# swap2(0, 4, nums)
# print(nums)

nums = [2, 5, 3, 4, 1] # unsorted

# the idea is we pass through the array n-1 times, where n is the len of the array
# we use n-1 because in the last iteration, we will only be left with the smallest element and no swap will be required
# for each pass, largest item will be moved to the right most position
# for each element, we see if it is out of order with the element on its right
# since the largest item will be at the right most after each pass, we need to reduce the n by 1 after each pass
# imagine after first pass, the largest item will be in index n-1, after second pass, the second largest item will be in index n-2
# we can terminate the algorithm early if we detect that no swaps was made in the first pass, meaning that the array is already sorted
def bubblesort(nums):
    n = len(nums)
    swapped = False
    for i in range(n-1): # loop for n-1 times, recall that this is because we can skip the last iteration whereby the element is always the smallest
        # the i part is just to specify the number of passes
        # the j index is the one which we will use to access the element at a position and also its neighbour.
        for j in range(n-1-i): # the last i elements would have already be sorted
            if nums[j] > nums[j+1]:
                swap(j, j+1, nums)
                if not swapped:
                    swapped = True
        if not swapped: # if after any pass, there is no swap, can terminate early
            break
    

print(nums) # unsorted
bubblesort(nums)
print(nums) # sorted