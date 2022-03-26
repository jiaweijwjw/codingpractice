to_be_sorted = [2, 8, 5, 3, 9, 4, 7, 1]

def merge(left_array, right_array):
    merged_array = []
    while left_array and right_array:
        if left_array[0] > right_array[0]:
            merged_array.append(right_array.pop(0))
        if right_array[0] > left_array[0]:
            merged_array.append(left_array.pop(0))
    if left_array:
        merged_array.append(left_array.pop(0))
    if right_array:
        merged_array.append(right_array.pop(0))
    return merged_array

def mergesort(to_be_sorted):
    n = len(to_be_sorted)
    if n == 1:
        return to_be_sorted
    left_array = to_be_sorted[:n//2]
    right_array = to_be_sorted[n//2:]
    left_array = mergesort(left_array)
    right_array = mergesort(right_array)
    return merge(left_array, right_array)

print(mergesort(to_be_sorted))