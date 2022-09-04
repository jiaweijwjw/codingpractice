# https://leetcode.com/problems/combination-sum/

class Solution():
    def __init__(self) -> None:
        pass

    def get_distinct_combinations(self, candidates, target):
        combinations = []
        def dfs(candidates, sum, combi):
            nonlocal combinations
            if sum == target:
                combinations.append(combi)
                return
            elif sum > target:
                return
            for i, num in enumerate(candidates): 
                dfs(candidates[i:], sum+num, combi[:]+[num]) # list + [element]
        dfs(candidates, 0, [])
        return combinations

    # this solution doesnt solve the unique part
    def get_distinct_combinations2(self, candidates, target):
        combinations = []
        def dfs(sum, combi):
            nonlocal combinations
            if sum == target:
                combinations.append(combi)
                return
            elif sum > target:
                return
            for num in candidates: # sum < target
                new_combi = combi[:]
                new_combi.append(num)
                dfs(sum+num, new_combi)
        dfs(0, [])
        return combinations


if __name__ == "__main__":
    solution = Solution()
    inputs = [([2,3,6,7],7),([2,3,5],8),([2],1)]
    # outputs: [[2,2,3],[7]], [[2,2,2,2],[2,3,3],[3,5]], []
    for candidates, target in inputs:
        print(solution.get_distinct_combinations(candidates, target))