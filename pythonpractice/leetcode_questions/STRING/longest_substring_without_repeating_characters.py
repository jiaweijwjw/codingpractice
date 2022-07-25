sample_strings = [
    "abcabcbb", # 3
    "bbbbb", # 1
    "pwwkew", # 3
    "dvdf" # 3
]

# the basic idea of this question is that we iterate from start to end of the string
# and keep a count of the longest substring that is not repeated
# but what happens when a repeated char is seen?
# we want to continue from where the previous repeated char was seen
# for example, for "abcabcbb", when the second 'a' is seen, we want to continue from index 1 char 'b' by removing the first 'a'

# the following solution is naive because it does not backtrack, it completely resets from the repeated char part
# will not work for "dvdf"
def solution(str):
    longest_so_far = 0
    curr_substr_len = 0
    curr_chars = []
    for i in range(len(str)):
        if str[i] not in curr_chars: # not a repeated char
            curr_chars.append(str[i])
            curr_substr_len += 1
            longest_so_far = max(longest_so_far, curr_substr_len)
        else: # repeated char
            curr_chars = [str[i]]
            curr_substr_len = 1
    return longest_so_far

# what if i store the positions too, then i take out from repeated element and before
# to check for repeation, we can usually use a set but in this case, we use a list so we can know the index
def solution2(str):
    longest_so_far = 0
    curr_substr_len = 0
    curr_chars = [] # store tuples?
    for i in range(len(str)):
        if str[i] not in curr_chars:
            curr_chars.append(str[i])
            curr_substr_len += 1
        else: # we handle here differently as compared to solution 1
            pos = curr_chars.index(str[i])
            curr_chars = curr_chars[pos+1:] # remove everything from the front, since we appended, its in order
            curr_chars.append(str[i])
            curr_substr_len = len(curr_chars)
        longest_so_far = max(longest_so_far, curr_substr_len)
    return longest_so_far

# to further improve solution2, we can see that by storing the curr_chars as a list, we incur O(N) space
# also, checking for existence in a list is O(N) time
# as mentioned, to check for existence, we can usually use a set or dict
# since we want to keep track of the index, we will use a dict instead
# in this case, our checking for existence will be O(1) and space is also O(1) as there are 26 characters
def solution3(str):
    longest_substr_len = 0
    start = 0
    curr_chars = {}
    for i in range(len(str)): # we require the index so use this index based for loop
        # other than just checking for existence, we have to check that the index is not before start, because anything before is ignored
        # in solution2, we removed/chopped off everything from infront of the previous repeated char
        # but for the dict, we didnt remove it
        # for example in "abcba", when 'b' is seen again, start moves to index 1. 
        # when the second 'a' is seen, the previous 'a' is still in the dictionary with index 0, but we already ignore this as start is at index 1
        if str[i] in curr_chars and curr_chars[str[i]] >= start: # repeated char
            start = curr_chars[str[i]]+1 # move start to the next char after the previous repeated char
        curr_chars[str[i]] = i # set the index of the new char
        longest_substr_len = max(longest_substr_len, i-start+1)
    return longest_substr_len



for str in sample_strings:
    print(solution(str))
print()
for str in sample_strings:
    print(solution2(str))
print()
for str in sample_strings:
    print(solution3(str))