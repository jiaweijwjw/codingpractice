# this question can be solved using a variety of methods
# to understand the questions, draw out the paths , tree to show what are the steps needed to take

num_of_parentheses = [n for n in range(1, 5)]
# num_of_parentheses = [3]

# using recursion
# for recursion, we have to identify the base case
# in this case, the base case is when both left and right is 0, then we add the final answer to the list
# 2 important things to take note that i missed:
# firstly, remember to return during the base case
# secondly, remember to use parenthese in if clauses, if not there could be hard to find bugs
# next, we will always maintain the 2 counters left and right such that at any time, left is <= right,
# meaning that right will never be less than left.
# this is so that we ensure that the parentheses are in proper order
def solution(n):
    ans = []
    parens = "" # for clarify, if not can use keyword argument
    left, right = n, n # for clarify, if not can use keyword argument
    generate(ans, left, right, parens)
    return ans


def generate(ans, left, right, parens):
    # print(left, right, parens)
    if left == 0 and right == 0:
        ans.append(parens)
        return
        # DONT FORGET TO TERMINATE HERE OR IT WILL GO INTO THE NEXT IF CLAUSE
    elif left == right: #  and (left and right > 0) no need to write this actually
        generate(ans, left-1, right, parens=parens + "(")
    elif left < right and left > 0:
        generate(ans, left, right-1, parens=parens + ")")
        generate(ans, left-1, right, parens=parens + "(")
    elif left == 0 and right > 0:
        generate(ans, left, right-1, parens=parens + ")")

for n in num_of_parentheses:
    print(solution(n))
