from collections import Counter
ransomNote = "aaa"
magazine = "aab"

# this is a very simple questions
# the idea is that we take all characters in magazine and store the count of each char in a char_bank dict
# then for each char in ransomNote, we try to find the char in char_bank
# if it does not exist, we can exit early
# else if at the end of the iteration, and there is no early exit, it means that ransomNote can be constructed from chars in char_bank
def solution(ransomNote, magazine):
    char_bank = {}
    for char in magazine:
        if char not in char_bank:
            char_bank[char] = 1
        else:
            char_bank[char] += 1
    for char in ransomNote:
        if char not in char_bank:
            return False
        else:
            if char_bank[char] == 1:
                char_bank.pop(char)
            else:
                char_bank[char] -= 1
    return True

# using python Counter module, we can do a one liner:
# note that we are take ransomNote - magazine, NOT magazine - ransomNote
# what this does is that it checks whether all char in ransomNote is in magazine
# if all char in ransomNote is in magazine, the final Counter will be empty
# if there is some char in ransomNote that is not in magazine, these chars will be in the remaining counter
def solution2(ransomNote, magazine):
    # print(Counter(ransomNote))
    # print(Counter(magazine))
    ans = Counter(ransomNote) - Counter(magazine)
    # print(ans)
    print(not ans)

print(solution(ransomNote, magazine))
solution2(ransomNote, magazine)