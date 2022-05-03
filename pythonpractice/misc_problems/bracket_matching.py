# for each equations provided, check if the brackets used are correct

eqn1 = "{(a+b)*(c*d)}" # correct
eqn2 = "[{(2a)(2b)}/(3c)]" # correct
eqn3 = "[{(2a)(2b)}/(3c)]]" # wrong

opening_brackets = ['[', '{', '(']
closing_brackets = [']', '}', ')']

def check_brackets(equation):
    stack = [] # using a list as stack, can try importing linked list to use as stack also
    for char in equation:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack: # stack not empty
                prev_bracket = stack.pop()
            else: # terminate early
                return
            if prev_bracket in opening_brackets and (opening_brackets.index(prev_bracket) == closing_brackets.index(char)):
                continue
            else: # terminate early
                return
    if stack: # still got things in the stack after parsing through entire string
        return
    else:
        return "Brackets in this equation is correct."

print(check_brackets(eqn1))
print(check_brackets(eqn2))
print(check_brackets(eqn3))
