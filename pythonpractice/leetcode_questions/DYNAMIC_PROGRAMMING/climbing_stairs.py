class Solution():
    def __init__(self) -> None:
        pass

    # this recursive solution works in terms of logic, but time limit exceeds when the number of steps get too big
    def get_num_of_distinct_ways_recursive(self, n):
        num_of_ways = 0
        def recurse(n):
            nonlocal num_of_ways
            if n == 0:
                num_of_ways += 1
            for step_count in range(1, 3): # 1 based indexing. only can take 1 or 2 steps for this question
                if (n-step_count) >= 0:
                    recurse(n-step_count)
        recurse(n)
        return num_of_ways

    # now, we will improve on the above solution by adding memoization. what this means is that we dont need to calculate again
    # this is a more generic way of writing
    def get_num_of_distinct_ways_recursive_with_memoization(self, n): # top down
        cache = {}
        cache[1], cache[2] = 1, 2 # prepopulate some base case
        def recurse(n):
            nonlocal cache
            if n == 0:
                return 1 # instead of returning 0. draw the whole tree to understand why. basically counting how many 0 we can reach
            # elif n == 1:
            #     return 1
            # elif n == 2:
            #     return 2
            num_ways_for_this_amount_of_steps = 0
            for i in range(1, 3): # we can only take steps of 1 or 2
                remaining_steps = n-i
                if remaining_steps >= 0:
                    num_ways_for_remaining_steps = cache[remaining_steps] if remaining_steps in cache else recurse(remaining_steps)
                    num_ways_for_this_amount_of_steps += num_ways_for_remaining_steps
            cache[n] = num_ways_for_this_amount_of_steps
            return num_ways_for_this_amount_of_steps
        num_of_ways = recurse(n)
        return num_of_ways if n in cache else -1

    def get_num_of_distinct_ways_bottom_up(self, n):
        if n <= 2:
            return n
        cache = [0]*(n+1) # using 1 based indexing
        cache[1], cache[2] = 1, 2 # if n is < 2 here will index out of error, so we manually return early above
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

            

if __name__ == "__main__":
    solution = Solution()
    steps = [2,3,4,5] # 2,3,5
    for n in steps:
        print(solution.get_num_of_distinct_ways_recursive(n))
        print(solution.get_num_of_distinct_ways_recursive_with_memoization(n))
        print(solution.get_num_of_distinct_ways_bottom_up(n))