# https://leetcode.com/problems/house-robber/

class Solution():
    def __init__(self) -> None:
        pass

    # can rob from the front also, doesnt matter
    def get_max_loot(self, houses):
        if len(houses) <= 2: # 1 or 2 houses, just rob the one with the most money
            return max(houses)
        loot_cache = houses[:] # clone
        for i in range(len(houses)-3, -1, -1):
            for j in range(i+2, len(loot_cache)):
                loot_cache[i] = max(loot_cache[i], houses[i] + loot_cache[j]) # note here we add to original houses[i], if not we will use the already updated value by previous iteration which is wrong
        return max(loot_cache)

if __name__ == "__main__":
    solution = Solution()
    inputs = [[1,2,3,1],[2,7,9,3,1]]
    # outputs: 4, 12
    for houses in inputs:
        print(solution.get_max_loot(houses))