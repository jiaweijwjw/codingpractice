# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution():
    def __init__(self) -> None:
        pass

    def get_length_of_longest_substring_without_repeating_characters(self, string):
        longest = 0
        start = 0
        checked = {}
        for i, char in enumerate(string):
            if char in checked and checked[char] >= start:
                start = checked[char] + 1
            checked[char] = i
            longest = max(longest, i-start+1)
        return longest

if __name__ == "__main__":
    solution = Solution()
    inputs = ["abcabcbb","bbbbb","pwwkew"]
    # outputs: 3, 1, 3
    for string in inputs:
        print(solution.get_length_of_longest_substring_without_repeating_characters(string))