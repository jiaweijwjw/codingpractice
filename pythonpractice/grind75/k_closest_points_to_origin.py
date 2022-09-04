# https://leetcode.com/problems/k-closest-points-to-origin/
from heapq import heappush, nsmallest
from math import sqrt

class Solution():
    def __init__(self) -> None:
        pass

    def get_k_closest_points(self, points, k):
        distance_heap = [] # (distance, point)
        for point in points:
            distance = self.calculate_distance(point)
            heappush(distance_heap, (distance, point))
        return [point for (dist, point) in nsmallest(k, distance_heap)]

    def calculate_distance(self, point):
        return sqrt(point[0]**2+point[1]**2)

if __name__ == "__main__":
    solution = Solution()
    inputs = [([[1,3],[-2,2]],1),([[3,3],[5,-1],[-2,4]],2)]
    # outputs: [[-2,2]], [[3,3],[-2,4]]
    for points, k in inputs:
        print(solution.get_k_closest_points(points, k))