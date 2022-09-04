# https://leetcode.com/problems/insert-interval/

class Solution():
    def __init__(self) -> None:
        pass

    def insert_interval(self, intervals, new_interval):
        left, right = [], []
        start, end = new_interval # unpacking
        for interval in intervals:
            if self._is_overlap_with_new_interval(interval, new_interval):
                start, end = self._merge_intervals([start, end], interval)
            else:
                if interval[1] < start:
                    left.append(interval)
                elif interval[0] > end:
                    right.append(interval)
        return left + [[start, end]] + right

    def _is_overlap_with_new_interval(self, interval, new_interval):
        return interval[1] >= new_interval[0] and interval[0] <= new_interval[1] # and not or

    def _merge_intervals(self, prev, curr):
        return (min(prev[0], curr[0]), max(prev[1], curr[1]))

if __name__ == "__main__":
    solution = Solution()
    inputs = [([[1,3],[6,9]],[2,5]),([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])]
    # outputs: [[1,5],[6,9]], [[1,2],[3,10],[12,16]]
    for intervals, new_interval in inputs:
        print(solution.insert_interval(intervals, new_interval))