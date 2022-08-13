# https://leetcode.com/problems/valid-anagram/

class Solution():
    def __init__(self) -> None:
        pass

    def is_anagram(self, s, t):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char in char_count:
                if char_count[char] == 1:
                    del char_count[char]
                else:
                    char_count[char] -= 1
            else:
                return False
        if char_count:
            return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    inputs = [("anagram","nagaram"),("rat","car")]
    # outputs: true, false
    for s, t in inputs:
        print(solution.is_anagram(s, t))