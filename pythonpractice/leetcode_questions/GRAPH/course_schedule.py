# https://leetcode.com/problems/course-schedule/

class Solution():
    def __init__(self) -> None:
        pass

    def can_finish(self, num_courses, prereqs):
        visited = [0 for _ in range(num_courses)] # store 3 states, 
        # -1 for currently visiting in this dfs cycle, 
        # # 0 for not visited, 
        # 1 for visited, dont need to check again (but not considered a cycle)
        adj_list = [[] for _ in range(num_courses)] # can use dict or list, but since the course num is contiguous, we can use a list, to use less space
        # rmb cant use [[]]*num_courses as the list object will be referencing to the same object
        for course, prereq in prereqs: # unpack the 2-list (list of 2 elements)
            adj_list[course].append(prereq)

        def dfs(course) -> bool:
            if visited[course] == -1: # cycle is detected in this dfs cycle
                return False
            elif visited[course] == 1: # dont have to continue checking from here as it has been checked
                return True
            else: # unvisited
                visited[course] = -1 # mark as visiting in this dfs cycle
                for prereq in adj_list[course]:
                    if not dfs(prereq):
                        return False # anytime a cycle is detected, we can just stop checking already
                visited[course] = 1 # only after checking all the neighbours and returning to the parent (recursive), then we make a node as visited
                return True

        # we have to run dfs for every node as the graphs may not be connected components
        # if any connected component has a cycle, exit the for loop early, dont have to continue checking
        for course in range(num_courses):
            if not dfs(course):
                return False
        return True

# we are using DFS to check for DAG
# we can create another individual visited for every dfs cycle, but that would take more space.
# instead, we just use 3 states instead of the usual, in visited or not in visited 2 states
# the visiting state if for us to keep track of cycles in this current dfs cycle
# the visited state is just to not redo work that has done previously
# think of the purpose of the visited state is so that we ensure the entire graph is accounted for as there may be non connected compoenents
# the dfs function will return True or False to tell if this dfs cycle has a cycle
# at any one time, if any connected component has a cycle, we do not have to check the remaining components

# another method could be to do topological sorting?

if __name__ == "__main__":
    solution = Solution()
    inputs = [(2,[[1,0]]),(2,[[1,0],[0,1]])]
    # outputs: True, False
    for num_courses, prereqs in inputs:
        print(solution.can_finish(num_courses, prereqs))