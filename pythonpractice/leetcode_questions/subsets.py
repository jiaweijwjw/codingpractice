nums = [1, 2, 3]

def solution(nums):
    ans = []
    subset = []
    get_subsets(ans, nums, subset) # start with empty subset
    return ans

def get_subsets(ans, nums, subset):
    # print(subset)
    ans.append(subset[:])
    if not nums:
        return
    for i in range(len(nums)):
        subset.append(nums[i])
        # ans.append(subset[:])
        if i == len(nums)-1:
            # return
            get_subsets(ans, [], subset[:]) # after this will enter the not nums condition
            subset.pop(len(subset)-1) # this line is important to pop back out during backtracking
        else:
            get_subsets(ans, nums[i+1:], subset[:])
            subset.pop(len(subset)-1)


# solution2 is much more efficient and uses the recursion trick
# see below for a quick revision of my observations on recursion from the following questions: generate_parentheses, combinations and subsets
def solution2(nums):
    ans = []
    get_subsets2(ans, nums, 0, [])
    return ans

def get_subsets2(ans, nums, index, subset):
    ans.append(subset)
    for i in range(index, len(nums)):
        clone_subset = subset[:]
        clone_subset.append(nums[i])
        get_subsets2(ans, nums, i+1, clone_subset)
        

print(solution2(nums))

# another way of doing list.append(element) is list+[element]
# test = [1]
# test = test+[2]
# print(test)

# recursion technique:
# we can think of recursion like our graphs and trees
# so usually the decision paths can be draw out in a tree-like format
# draw the ENTIRE tree including those paths that you are supposed to exit
# from there, we can come up with the base cases for our recursion
# the base cases usually includes conditions to not take a certain path AND in all cases, the final step / leaf node if u imagine it like a tree
# to make the base cases easy to handle, we try to modify all values before passing it into the next recursion
# this is so we can just exit if it is not the path we want to take or return values if needed in a final / end / leaf case
# an analogy is to consider traversing a graph, we ENTER the next node after a leaf node, then EXIT if it is None
# recursion is actually like DFS because it uses a stack, this means that we always enter deep till the end instead of like BFS
# if the recursion tree is binary like (like in generate parenthese), we can just call the recursive function twice on the left and right
# if the tree can have many branches instead, we can use a for loop
# note that in using a for loop, we usually have to clone the values such as cloning the list
# if not, all iterations of the for loop will use the same object and this will lead to wrong results

