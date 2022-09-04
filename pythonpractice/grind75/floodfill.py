# https://leetcode.com/problems/flood-fill/

directions = [(0,1),(1,0),(0,-1),(-1,0)]

class Solution():
    def __init__(self) -> None:
        pass

    def flood_fill(self, image, sr, sc, color):
        starting_pixel_color = image[sr][sc]
        visited = set()
        def dfs(c, r):
            visited.add((c, r))
            image[r][c] = color
            for dir in directions:
                neighbour_c = c + dir[0]
                neighbour_r = r + dir[1]
                if self._within_bounds(image, neighbour_c, neighbour_r) and (neighbour_c, neighbour_r) not in visited and image[neighbour_r][neighbour_c] == starting_pixel_color:
                    dfs(neighbour_c, neighbour_r)
        dfs(sc, sr)
        return image

    def _within_bounds(self, image, c, r):
        return 0 <= r <= len(image)-1 and 0 <= c <= len(image[0])-1

if __name__ == "__main__":
    solution = Solution()
    inputs = [([[1,1,1],[1,1,0],[1,0,1]],1,1,2),([[0,0,0],[0,0,0]],0,0,0)]
    # outputs: [[2,2,2],[2,2,0],[2,0,1]], [[0,0,0],[0,0,0]]
    for image, sr, sc, color in inputs:
        image = solution.flood_fill(image, sr, sc, color)
        for row in image:
            print(row)
        print()