from math import inf

class Solution():
    def __init__(self) -> None:
        pass

    # this is a interval scheduling greedy algorithm
    # same idea as: fitting most number of activities in a day without any time overlap
    def num_of_intervals_to_remove(self, intervals):
        count = 0
        end = -inf # the furthest end so far
        intervals.sort(key=lambda x: x[1]) # sort by the end time
        for left, right in intervals: # list unpacking because we know the list only contains exactly 2 elements
            if left >= end:
                end = right # extend the furthest end
            else:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,2],[1,2],[1,2]]
    print(solution.num_of_intervals_to_remove(intervals))