class Solution():
    def __init__(self) -> None:
        pass

    # how to differentiate the left and the right
    def insert_interval(self, intervals, new_interval):
        left, right = [], []
        start, end = new_interval # cannot init to inf, -inf. will encounter wrong result if you try [[1,3],[6,9]] insert [2,5]
        for interval in intervals:
            if self.is_overlap_new_interval(interval, new_interval):
                start, end = self.merge([start, end], interval)
            else:
                if interval[1] < start:
                    left.append(interval)
                elif interval[0] > end:
                    right.append(interval)
        return left + [[start, end]] + right # list + [element]

    def is_overlap_new_interval(self, interval, new_interval):
        return interval[1] >= new_interval[0] and interval[0] <= new_interval[1]

    def merge(self, prev_interval, curr_interval):
        return (min(prev_interval[0], curr_interval[0]), max(prev_interval[1], curr_interval[1])) # tuple (start, end)


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(solution.insert_interval(intervals, new_interval))