from math import sqrt
from heapq import heappush, nsmallest
points = [[3,3],[5,-1],[-2,4]]
k = 2


class Solution():
    def __init__(self, points, k) -> None:
        self.points = points
        self.k = k
        self.heap = []

    def calc_dist(self, x, y):
        return sqrt(x**2+y**2)

    def get_k_closest_points_to_origin(self):
        for point in self.points:
            x, y = point[0], point[1]
            heappush(self.heap, (self.calc_dist(x, y), point))
        return [point[1] for point in nsmallest(k, self.heap)]
        
solution = Solution(points, k)
print(solution.get_k_closest_points_to_origin())