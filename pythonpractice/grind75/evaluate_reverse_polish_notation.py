# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from collections import deque
from operator import add, sub, mul, truediv

use_operator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}
class Solution():
    def __init__(self) -> None:
        pass

    # cannot check numeric as negative numbers has a dash sign "-"
    def evaluate_notation(self, tokens):
        s = deque()
        for token in tokens:
            if token in use_operator: # is operator
                # we assume that can always be evaluated, wont have error input
                operand2 = s.pop() # operand2 comes out of the stack first
                operand1 = s.pop()
                s.append(int(use_operator[token](operand1, operand2)))
            else:
                s.append(int(token)) # change string to int
        ans = s.pop()
        return ans

if __name__ == "__main__":
    solution = Solution()
    inputs = [(["2","1","+","3","*"]),(["4","13","5","/","+"]),(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])]
    # outputs: 9, 6, 22
    for tokens in inputs:
        print(solution.evaluate_notation(tokens))

