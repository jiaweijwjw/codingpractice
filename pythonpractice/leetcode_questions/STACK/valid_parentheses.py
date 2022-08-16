sample_s = ["()", # true
            "()[]{}", # true
            "(]", # false
            "(", # false
            ")"] # false. this is an edge case of popping from empty stack

def solution(s):
    stack = []
    opening_brackets = {"(": ")", 
                        "[": "]", 
                        "{": "}"}
    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else: # is closing bracket
            if not stack: # edge case if the first one is a closing bracket and u try to pop from empty stack, will have error
                return False
            prev_bracket = stack.pop()
            if bracket != opening_brackets[prev_bracket]:
                return False
    if stack: # if there is remaining items in the stack, if only 1 char in the string s, this will occur
        return False
    else:
        return True

for s in sample_s:
    print(solution(s))