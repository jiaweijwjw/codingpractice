# https://leetcode.com/problems/course-schedule/

class Solution():
    def __init__(self) -> None:
        pass

    def can_finish(self, num_courses, prereqs):
        visited = [0 for _ in range(num_courses)] # store 3 states, 
        adj_list = [[] for _ in range(num_courses)] 

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
                        return False 
                visited[course] = 1 # only after checking all the neighbours and returning to the parent (recursive), then we make a node as visited
                return True

        for course in range(num_courses):
            if not dfs(course):
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    inputs = [(2,[[1,0]]),(2,[[1,0],[0,1]])]
    # outputs: True, False
    for num_courses, prereqs in inputs:
        print(solution.can_finish(num_courses, prereqs))