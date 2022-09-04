# https://leetcode.com/problems/maximum-subarray/

class Solution():
    def __init__(self) -> None:
        pass

    def get_max_sum_subarray(self, arr):
        if len(arr) == 1:
            return arr[0]
        left = 0
        right = 1
        curr_sum = max_sum = arr[0]
        while right <= len(arr)-1:
            sum = curr_sum + arr[right]
            if sum < arr[right]: # this part need to write out to see
                left = right
                curr_sum = arr[left]
                right = left + 1
            else:
                curr_sum = sum
                right += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum
            


if __name__ == "__main__":
    solution = Solution()
    inputs = [[-2,1,-3,4,-1,2,1,-5,4],[1],[5,4,-1,7,8]]
    # outputs: 6, 1, 23
    for arr in inputs:
        print(solution.get_max_sum_subarray(arr))