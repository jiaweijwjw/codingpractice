# https://leetcode.com/problems/minimum-window-substring/
# this question is similar to find_all_anagrams_in_a_string
from math import inf 
class Solution():
    def __init__(self) -> None:
        pass

    # we are using a sliding window technique whereby window size is not fixed and can be variable
    # the window is slided by moving the right pointer. keep sliding this pointer till we find a valid window
    # in this case, a valid window is a substring which has all the characters in t
    # note that we must have ALL the characters and also the count of characters must be >= the count of the character in t_dict
    # this is the part where we cannot do it exactly the same as the find_all_anagrams_in_a_string question
    # for that question, we can just compare the window dict with the string in comparison dict
    # for this question, the idea is the same but we cannot compare the dict directly, hence we keep track by using additional variables
    def get_minimum_window_substring(self, s, t):
        left = right = 0 # pointers for window
        t_dict = {}
        window = {}
        min_window = (left, right) # keeps track of the window that is the min
        min_window_size = inf # we need to return empty string if not found so we cant just init to len(s)
        # populate t_dict
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        num_unique_chars_in_t_dict = len(t_dict)
        def is_valid_window(meets_criteria_count):
            return meets_criteria_count == num_unique_chars_in_t_dict
        # 2 pointers start and end / left and right represents a window
        # move end/right to find a valid window
        # when a avlid window is found, move start to find a smaller window
        meets_criteria_count = 0
        while right <= len(s)-1:
            right_char = s[right]
            if right_char in t_dict:
                window[right_char] = window.get(right_char, 0) + 1
                if window[right_char] >= t_dict[right_char]:
                    meets_criteria_count += 1
            if is_valid_window(meets_criteria_count):
                new_window_size = right - left + 1
                if new_window_size < min_window_size:
                    min_window_size = new_window_size
                    min_window = (left-1, right)
                while is_valid_window(meets_criteria_count) and left < right:
                    left_char = s[left]
                    if left_char in window and left_char in t_dict: # or in t_dict
                        if window[left_char]-1 < t_dict[left_char]:
                            meets_criteria_count -= 1
                        if window[left_char] == 1:
                            del window[left_char]
                        else:
                            window[left_char] -= 1
                    left += 1
            right += 1
        # print(min_window)
        # print(window)
        # print(t_dict)
        return s[min_window[0]:min_window[1]+1] if min_window_size is not inf else "" # slice only the selected elements

if __name__ == "__main__":
    solution = Solution()
    inputs = [("ADOBECODEBANC","ABC"),("a","a"),("a","aa")]
    # outputs: "BANC", "a", ""
    for s, t in inputs:
        print(solution.get_minimum_window_substring(s, t))