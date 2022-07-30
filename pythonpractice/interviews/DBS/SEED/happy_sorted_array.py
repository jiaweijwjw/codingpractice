nums_list = [
    [10,22,9,33,21,50,41,60], # 2
    [1,2,3,4,5], # 0
    [1,2,3,5,4], # 0
    [1], # 0
    [5,4,3,2,1] # 3
]

# this solution is a O(n^2) solution, using dynamic programming
# to come up with the DP solution, we usually think of how we are going to solve the problem in the brute force way
# in this case, the simple (brute force) way would be to take each number, and then compare with every sub array behind it
# for example, taking the array [1,2,3,4,5], for the current number 1, we first go through every number from 2 to 5 and count what is the length of the largest increasing sequence
# then, with the same current number 1, we then go through every number from 3 to 5 and count what is the length of the largest increasing sequence
# we do this for every sub array behind the current number [2,3,4,5], [3,4,5], [4,5], [5] and then store the value of the longest increasing sequence only
# using this idea, we can apply the same idea backwards, meaning taking the starting current number as 5
# and checking for every subarray before it, [4,3,2,1], [3,2,1], [2,1], [1]
# it is not a necessary step to think of it backwards, but just easier to go through by hand as we want to start from the front in our DP solution
# firstly, how to know that we can use a DP solution is that notice that we will need to do certain recalculations again even though it is already done
# for example, lets say after calculating the LIS of 5 in the backwards bruteforce way, the next number is 4
# the remaining subarrays to be calculated are [3,2,1], [2,1], [1] which is actually already calculated when we were checking for number 5
# now, we will move on to the harder part
# what it means to start from the front in the DP solution is:
# for every number 1 to 5, we check the subarrays before it and store the largest LIS (longest increasing subsequence length)
# to store the LIS, we need to initialize a buffer (list) to hold the LIS up to and including the current number
# for example, starting at 1, for every number before 1, if 1 is larger than that number, we update LIS of 1
# since no number is before 1, the LIS of 1 is 1
# next, we move on to number 2. for every number before 2 (which is only the number 1), since 2 is larger than 1,
# we take the max(current LIS of 2, LIS at 1 plus 1) which is max(1, 2) = 2
# the plus 1 is because since 2 > 1, we want to extend the LIS, meaning the LIS at 2 includes the subarray of 1
# next, we move on to number 3, for every number before 3 ( which is numbers 1 and 2), 
# since 3 > 1, we take max(current LIS of 3, LIS at 1 plus 1) which is max(1, 1) = 1
# since 3 > 2, we take max(current LIS of 3, LIS at 2 plus 1) which is max(1, 2) = 2
# note that this is the magic of DP. when we are calculating 3 vs the number 2, the LIS at 2 is already 2, because previously it was already calculated the the LIS at 2 includes 1 in the subarray
# to further explain this, we will use another example [10,22,9,33,21,50,41,60]
# starting at the number 10, LIS will be 1
# next the number 22, since 22 > 10, we take max(current LIS of 22, LIS at 10 plus 1) which is max(1,2)
# next is the number 9, since 9 < 10 and 9 < 22 it maintains its current LIS of 1
# next is the number 33, we have to check every subarray till every number before it. i.e subarray before 10, subarray before 22 and subarray before 9
# since 33 > 10, we take max(current LIS at 33, LIS at 10 plus 1) which is max(1,2) = 2
# moving on to the next subarray till 22, since 33 > 22, we take max(current LIS at 33, LIS at 22 plus 1) which is max(1,3) = 3
# moving on to the next subarray till 9, since 33 > 9, we take max(current LIS at 33, LIS at 9 plus 1) which is max(3,2) = 3
# this is why we use the max() because even though 33 > 9, the length of subsequence [10,22,33] is larger than the length of subsequence [9,33]

class Solution():
    def __init__(self, n, nums) -> None:
        self.n = n
        self.nums = nums

    def answer(self):
        if self.n == 1: # exit early
            return 0
        longest_subsequence = self.find_LIS()
        if longest_subsequence == self.n or longest_subsequence == self.n-1: # already sorted or only 1 element out of place
            return 0
        else:
            return self.n - longest_subsequence - 1 # the -1 is just specific to this happy sorted array problem
        
    def find_LIS(self):
        LIS = [1]*self.n
        # LIS is the longest increasing subsequence and we are calculating the LIS up to the current num
        # we have to check the current LIS against all the LIS of each of the previous numbers
        for i in range(self.n):
            for j in range(0, i):
                if nums[i] > nums[j]: # only need to update LIS value if the current num is larger than number before it that we are checking in index j
                    LIS[i] = max(LIS[i], LIS[j]+1) # if it is larger, then we need to add this current number. we have to use max() because we are finding the largest sequence
                    # for example, 33 is larger than 10, so the LIS will be updated to 2
                    # 33 is also larger than 22, and since the LIS at 22 includes 10, the LIS at 33 will be updated to 2+1=3
                    # however, although 33 is larger than 9, the LIS at 9 is only itself, and 9, 33 is only a sequence length of 2, hence LIS at 33 will remain at 3
        return max(LIS)

if __name__ == "__main__":
    # n = input("please input array length N.")
    # nums = input("please input array of N nums separated with spaces.")
    # solution = Solution(n, nums)
    # print(solution.answer())
    for nums in nums_list:
        solution = Solution(len(nums), nums)
        print(solution.answer())