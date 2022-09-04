# https://leetcode.com/problems/climbing-stairs/

class Solution():
    def __init__(self) -> None:
        pass

    def get_distinct_ways(self, n):
        cache = [0]*(n+1) if n > 2 else [0]*3 # key = num of steps, value = number of ways to climb 'key' number of steps
        cache[1] = 1
        cache[2] = 2
        if n <= 2: # have to do this else have to initialize the cache to 1 for more generalization.
            return n
        def recurse(n): # returns number of ways for a certain number of steps
            nonlocal cache
            if n == 0: # reach base case, found 1 way
                return 1 # hence we return the num of ways = 1
            # we dont need to check for n == -1 because the condition will be checked in remaining number of steps
            # if the remaining numbers of steps goes to negative, we wont even further recurse the decision tree
            num_of_ways_for_current_num_of_steps = 0
            for step in range(1,3): # take either 1 step or 2 steps
                remaining_steps = n-step
                if remaining_steps >= 0: # this line is important so we only enter the next decision path if it is a valid step to take
                    num_of_ways_for_remaining_steps = cache[remaining_steps] if cache[remaining_steps] != 0 else recurse(remaining_steps) # cannot use 'in' as it will be too slow for array type cache
                    # if the num of ways for the remaining steps have already been calculated, fetch it
                    # else, we will count it for the first time by calling the recurse function
                    num_of_ways_for_current_num_of_steps += num_of_ways_for_remaining_steps
                    # num of ways depends on the num of ways for each of the path taken. either the 1 step path or the 2 step path
            cache[n] = num_of_ways_for_current_num_of_steps # save the num of ways for this amount of steps
            return num_of_ways_for_current_num_of_steps
        return recurse(n)


if __name__ == "__main__":
    solution = Solution()
    inputs = [2, 3, 4, 5]
    # outputs: 2, 3, 5, 8
    for n in inputs:
        print(solution.get_distinct_ways(n))

            # remaining_steps = n - level
            # if remaining_steps in cache:
            #     return cache[remaining_steps]
            # else:
            #     num_of_ways_from_this_level = 0
            #     for step in range(1, 3): # take 1 step or 2 steps
            #         next_level = level + step
            #         num_of_ways_from_this_level += recurse(next_level)
            #     cache[level] = num_of_ways_from_this_level
            #     return num_of_ways_from_this_level