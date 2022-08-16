# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution():
    def __init__(self) -> None:
        pass

    # if we sort the nums visually and put them on a number line, we can visualize all sequences
    # what do we notice? if a number-1 is not in nums, it is not the start of a sequence
    # so basically, using this rule / condition, we iterate through the nums array to find the numbers which are start of sequences
    # when a start of sequence is found, we try to see if the consecutive numbers after it exists in the nums_set
    # we use a set because checking for existence is O(1)
    # then just always update the longest length seen
    def get_longest_consecutive_sequence(self, nums):
        nums_set = set(nums)
        longest = 0
        def is_start_of_sequence(num):
            return num-1 not in nums_set
        for num in nums:
            curr_len = 0
            if is_start_of_sequence(num):
                while True:
                    if num not in nums_set:
                        break
                    num += 1
                    curr_len += 1
            longest = max(longest, curr_len)
        return longest

if __name__ == "__main__":
    solution = Solution()
    inputs = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    # outputs: 4, 9
    for nums in inputs:
        print(solution.get_longest_consecutive_sequence(nums))