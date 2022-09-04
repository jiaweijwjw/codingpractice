# https://leetcode.com/problems/valid-parentheses/

from collections import deque

brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Solution():
    def __init__(self) -> None:
        pass

    def is_valid_parentheses(self, string) -> bool:
        stack = deque()
        for bracket in string:
            if bracket in brackets: # opening
                stack.append(bracket)
            else: # closing
                if not stack:
                    return False
                prev_bracket = stack.pop()
                if brackets[prev_bracket] != bracket:
                    return False
        if stack:
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    inputs = ["()","()[]{}","(]"]
    # outputs: true, true, false
    for string in inputs:
        print(solution.is_valid_parentheses(string))
