n, k = 4, 2

# the following solution creates multiple of the same tree, we can actually try another method that uses backtracking on the same tree
def solution(n, k):
    ans = [] # we want this to be global
    if n == 1: # edge case
        return [[1]]
    for i in range(n, 0, -1):
        combinate(ans, i, k, []) # here we pass in a brand new list combi for each iteration
    return ans

def combinate(ans, n, k, combi):
    combi.append(n)
    print(n, combi)
    if len(combi) == k:
        ans.append(combi[:]) # this is important!! screenshot whatever was in the combi list, if not it will be reused
        print(f"ans = {ans}")
        return
    for i in range(n-1, 0, -1):
        combinate(ans, i, k, combi[:]) # if pass in like that, it will reuse the combi from the previous loop!!!
        # combi.pop(k-1) # this line would not work as it is too hard code

# solution 2 is exactly the same method as above but a much more cleaner code
def solution2(n, k):
    ans = []
    combinate2(ans, n, k, [])
    return ans

def combinate2(ans, n, k, combi):
    print(combi)
    if len(combi) == k:
        ans.append(combi)
        return
    for i in range(n, 0, -1):
        clone_combi = combi[:]
        clone_combi.append(i)
        combinate2(ans, i-1, k, clone_combi)

print(solution2(n, k))


# some comments for backtracking:
# Pick a starting point.
# while(Problem is not solved)
#     For each path from the starting point.
#         check if selected path is safe, if yes select it
#         and make recursive call to rest of the problem
#         before which undo the current move.
#     End For
# If none of the move works out, return false, NO SOLUTON.