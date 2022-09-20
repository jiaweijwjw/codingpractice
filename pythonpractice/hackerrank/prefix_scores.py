from math import inf

class Solution():
    def __init__(self) -> None:
        pass


    def get_prefix_scores(self, arr):
        ans = []
        max_till_i = -inf # we do this so we can calculate the max in O(1) instead of iterate through i times for each index to find the max
        prev_curr_max = -inf # this is to store the previous curr_max incase we have to use it for the faster way
        for i in range(len(arr)):
            score = 0
            if arr[i] > max_till_i: # found a new maximum
                max_till_i = arr[i] # set the new maximum
                curr_max = max_till_i
                # calculate everything again from 0 to i
                for j in range(i+1): # inclusive of this ith element
                    curr_sum = arr[j] + curr_max
                    score += curr_sum
                    curr_max = max(curr_max, curr_sum)
                prev_curr_max = curr_max # save this last curr_max value incase we need it in the shortcut stage
            else:
                print("shortcut")
                curr_max = max_till_i
                print("ans[i-1] + prev_curr_max + arr[i]")
                print(ans[i-1], "+", prev_curr_max, "+", arr[i])
                curr_sum = prev_curr_max + arr[i]
                curr_max = max(prev_curr_max, curr_sum)
                prev_curr_max = curr_max
                score = curr_sum + ans[i-1]
            ans.append(score%(10**9+7))
        return ans


if __name__ == "__main__":
    solution = Solution()
    inputs = [[1,2,3],[1,2,1],[5,1,4,2]]
    # outputs: [2,8,19], [2,8,14], [10,21,36,53]
    for arr in inputs:
        print(solution.get_prefix_scores(arr))