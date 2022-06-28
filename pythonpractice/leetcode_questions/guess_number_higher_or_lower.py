n = 10
pick = 6

class Solution():
    def __init__(self, pick) -> None:
        self.pick = pick

    def guess(self, num):
        # be careful about this, the actual number we are finding is actually pick, not num
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else: # num == pick
            return 0

    def guess_number(self, n):
        start, end = 1, n
        mid = (start+end)//2
        return self.binary_search(start, end, mid)

    def binary_search(self, start, end, mid):
        print(mid)
        if start > end:
            return
        num = self.guess(mid) 
        if num == 0:
            return mid
        elif num == 1: # search right
            start = mid+1
            mid = (start+end)//2
            return self.binary_search(start, end, mid)
        elif num == -1: # search left
            end = mid-1
            mid = (start+end)//2
            return self.binary_search(start, end, mid)
        else:
            return




solution = Solution(pick)
print(solution.guess_number(n))