# https://leetcode.com/problems/jump-game/

class Solution():
    def __init__(self) -> None:
        pass

    # def can_reach_end(self, nums) -> bool:
    #     if len(nums) == 1:
    #         return True
    #     checked = [False]*(len(nums)-1)
    #     left = right = 0
    #     while right < len(nums)-1: # break somewhere early??
    #         for i in range(left, right+1): # inclusive of right
    #             if not checked[i]: # this index has not been jumped from yet
    #                 if (i + nums[i]) >= len(nums)-1:
    #                     return True
    #                 if nums[i] == 0: break
    #                 left = right = i+1 # shift the windows
    #                 right = left + nums[i]
    #                 checked[i] = True
    #     return False

    def can_reach_end_greedy(self, nums):
        end_point = len(nums)-1
        for i in range(len(nums)-2, -1, -1): # start from second last element
            if i + nums[i] >= end_point:
                end_point = i # shift endpoint to that position
        return True if end_point == 0 else False

    # def can_reach_end_graph(self, nums):
    #     visited = [False]*len(nums)
    #     self.dfs(nums, 0, visited)
    #     return True if visited[len(nums)-1] else False

    # def dfs(self, nums, index, visited):
    #     if nums[index] == 0 or visited[index]:
    #         return
    #     visited[index] = True
    #     for next_index in range(min(index+nums[index], len(nums)-1), index, -1):
    #         self.dfs(nums, next_index, visited)
        



if __name__ == "__main__":
    solution = Solution()
    inputs = [[2,3,1,1,4],[3,2,1,0,4],[0,1],[0,2,3]]
    # outputs: true, false, false, false
    for nums in inputs:
        print(solution.can_reach_end_graph(nums))