sample_strings = [
    "abcabcbb", # 3
    "bbbbb", # 1
    "pwwkew" # 3
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

def solution2(str):
    pass

for str in sample_strings:
    print(solution(str))

for str in sample_strings:
    print(solution2(str))