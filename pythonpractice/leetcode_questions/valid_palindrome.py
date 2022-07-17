from curses.ascii import isalnum

# we can reverse a string and see if it is equal to itself
# another way is to use 2 pointers from the front and back and check for equality
# both is O(N) but the second method can exit early and allows for slightly faster time
# if we want to count the number of palindromes, we can also start from the middle and go outwards

sample_strings = [
    "A man, a plan, a canal: Panama", # true
    "race a car", # false
    "race car", # true
    " " # true
]

def solution(str):
    # filter out the non alpha numeric characters first
    # we do this by creating a new string with only the alphanumeric chars, and using the filter function
    # note that white spaces are removed too
    filtered_str = "".join(filter(isalnum, str)).lower()
    if not filtered_str: # empty string, exit early
        return True
    left = 0
    right = len(filtered_str)-1
    while left <= right: # include equal case for odd number of chars, will meet in the middle, meaning left = right
        if filtered_str[left] != filtered_str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

for str in sample_strings:
    print(solution(str))