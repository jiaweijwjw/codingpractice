# https://leetcode.com/problems/course-schedule/

# do dfs, then if not in visited or at the end got nodes not in visited, return False also

from collections import defaultdict

class Solution():
    def __init__(self) -> None:
        pass

    def can_finish_all_courses(self, num_of_courses, prereqs):
        adj_list = {course: [] for course in range(num_of_courses)}
        visited = set()
        can_finish = True
        for prereq in prereqs:
            course = prereq[0]
            dependency = prereq[1]
            adj_list[course].append(dependency)
        def dfs(course):
            nonlocal can_finish
            if not adj_list[course]:
                return
            if course in visited and adj_list[course]: # loop. if visited 
                can_finish = False
                return
            visited.add(course)
            for dependency in adj_list[course]:
                dfs(dependency)
            
        for course in adj_list:
            # visited.add(course)
            if not adj_list[course]: # no dependencies. note: empty lists are falsy
                continue
            else:
                # visited.add(course)
                dfs(course)

        return can_finish

if __name__ == "__main__":
    solution = Solution()
    inputs = [(2,[[1,0]]),(2,[[1,0],[0,1]])]
    # outputs: True, False
    for num_of_courses, prereqs in inputs:
        print(solution.can_finish_all_courses(num_of_courses, prereqs))