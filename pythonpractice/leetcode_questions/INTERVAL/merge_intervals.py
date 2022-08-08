class Solution():
    def __init__(self) -> None:
        pass

    def merge_intervals(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        ans = []
        prev, curr = 0, 1
        while curr < len(intervals):
            if self.is_overlap(intervals[prev], intervals[curr]):
                intervals[curr] = self.merge(intervals[prev], intervals[curr])
            else:
                ans.append(intervals[prev])
            if curr == len(intervals)-1:
                ans.append(intervals[curr])
            prev += 1
            curr += 1
        return ans
        
    def is_overlap(self, prev_interval, curr_interval) -> bool:
        return prev_interval[0] <= curr_interval[1] and curr_interval[0] <= prev_interval[1]

    def merge(self, prev_interval, curr_interval):
        return [min(prev_interval[0], curr_interval[0]), max(prev_interval[1], curr_interval[1])]

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge_intervals(intervals))