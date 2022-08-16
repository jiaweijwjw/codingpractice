class Solution():
    def __init__(self) -> None:
        pass

    def merge_intervals(self, intervals):
        if len(intervals) < 2: # must have at least 2 intervals to merge
            return intervals
        intervals.sort() # have to sort so we can merge properly from a single direction and getting correct answer
        ans = []
        prev, curr = 0, 1 # we already know at least 2 intervals
        while curr < len(intervals): # we will move the 2 pointers together. they are always sticked together. O(N) pass 
            if self.is_overlap(intervals[prev], intervals[curr]): # check if is overlap
                intervals[curr] = self.merge(intervals[prev], intervals[curr]) # HAVE TO assign to the curr interval on the right, not the prev interval
                # we are overwriting the latest interval value as this curr will be 'prev' in the next iteration
            else:
                ans.append(intervals[prev]) # if not overlap, we can add the latest merged interval into answer
            if curr == len(intervals)-1: # edge case. the last interval was not compared since we moving prev and curr together
                ans.append(intervals[curr])
            prev += 1
            curr += 1
        return ans
        
    def is_overlap(self, prev_interval, curr_interval) -> bool:
        return prev_interval[0] <= curr_interval[1] and curr_interval[0] <= prev_interval[1] # actually can just check for the end of prev <= the start of curr, since we already sort the intervals

    def merge(self, prev_interval, curr_interval):
        return [min(prev_interval[0], curr_interval[0]), max(prev_interval[1], curr_interval[1])]

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge_intervals(intervals))