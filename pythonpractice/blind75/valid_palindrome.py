# https://leetcode.com/problems/valid-palindrome/

class Solution():
    def __init__(self) -> None:
        pass

    def is_palindrome(self, string):
        string = "".join(filter(str.isalnum, string)).lower()
        if not string:
            return True
        start = 0
        end = len(string)-1
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    inputs = ["A man, a plan, a canal: Panama","race a car"," "]
    # outputs: true, false, true
    for string in inputs:
        print(solution.is_palindrome(string))