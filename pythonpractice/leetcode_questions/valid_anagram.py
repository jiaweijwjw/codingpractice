s = "anagram"
t = "nagaram"

def solution(s, t):
    if len(s) != len(t): # exit early
        return False
    else:
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char in t:
            if char in char_dict:
                if char_dict[char] == 1:
                    char_dict.pop(char) # remove this key entirely 
                else:
                    char_dict[char] -= 1
            else:
                return False # exit early
        if char_dict: # still has stuff in char dict, means not anagram
            return False
        else:
            return True
        
# another way to do it is just to sort the 2 strings and compare them
def solution2(s, t):
    if len(s) != len(t):
        return False
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    if sorted_s == sorted_t:
        return True
    else:
        return False

print(solution(s, t))
print(solution2(s, t))