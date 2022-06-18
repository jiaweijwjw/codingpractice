sample_strings = [
    "abcabcbb", # 3
    "bbbbb", # 1
    "pwwkew", # 3
    "dvdf" # 3
]

# the following solution will not work for "dvdf"
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
def solution2(str):
    longest_so_far = 0
    curr_substr_len = 0
    curr_chars = [] # store tuples?
    for i in range(len(str)):
        if str[i] not in curr_chars:
            curr_chars.append(str[i])
            curr_substr_len += 1
            longest_so_far = max(longest_so_far, curr_substr_len)
        else: # we handle here differently as compared to solution 1
            pos = curr_chars.index(str[i])
            curr_chars = curr_chars[pos+1:] # remove everything from the front, since we appended, its in order
            curr_chars.append(str[i])
            curr_substr_len = len(curr_chars)
    return longest_so_far

for str in sample_strings:
    print(solution(str))
print()
for str in sample_strings:
    print(solution2(str))