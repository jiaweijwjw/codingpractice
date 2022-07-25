s = "anagram"
t = "nagaram"

# to check if 2 strings are anagrams, there are a few ways, but we will look at the 2 common ways
# the first way is to sort both strings and check if they produce the same resulting string
# the time complexity is O(NlogN) and the space complexity would be O(N) (python's timsort)
# the next method is to do frequency counting of characters
# this will take O(N) time and O(1) space. O(1) because number of characters in character set is countable

# since the idea of this questions is to check whether every char in a string exists in another string,
# we can usually check existence by first putting all the available chars of the first string in a dict
# then for every char in the second string, we check if there is the char currently available in the dict
# if it is, then we take it out
# at any one time, if there is missing character, we can return the function early
# else if all the characters in string2 is already popped out from the dict, if there is any remaining items, we return False
# if not, the 2 strings are anagrams
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