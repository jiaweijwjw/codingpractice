from collections import deque

directions = [(0,1), (1,0), (0,-1), (-1,0)]

class Solution():
    def __init__(self) -> None:
        pass

    def _within_bounds(self, image, r, c):
        return 0 <= r <= len(image)-1 and 0 <= c <= len(image[0])-1

    def flood_fill_bfs(self, image, sr, sc, color):
        starting_color = image[sr][sc]
        q = deque()
        visited = set()
        q.append((sc, sr))
        while q:
            c, r = q.popleft()
            if (c, r) not in visited:
                visited.add((c, r))
                image[r][c] = color
                for dir in directions:
                    neighbour_c = c+dir[0]
                    neighbour_r = r+dir[1]
                    if self._within_bounds(image, neighbour_r, neighbour_c) and image[neighbour_r][neighbour_c] == starting_color:
                        q.append((neighbour_c, neighbour_r))
        return image

    def flood_fill_dfs(self, image, sr, sc, color):
        visited = set()
        starting_color = image[sr][sc]
        def dfs(image, r, c, color):
            nonlocal visited, starting_color
            if image[r][c] != starting_color:
                return
            visited.add((c, r))
            image[r][c] = color
            for dir in directions:
                neighbour_c = c+dir[0]
                neighbour_r = r+dir[1]
                if self._within_bounds(image, neighbour_r, neighbour_c) and (neighbour_c, neighbour_r) not in visited and image[neighbour_r][neighbour_c] == starting_color:
                    dfs(image, neighbour_r, neighbour_c, color)
        dfs(image, sr, sc, color)
        return image

    def flood_fill_dfs_iterative(self, image, sr, sc, color):
        starting_color = image[sr][sc]
        s = deque()
        visited = set()
        s.append((sc, sr))
        while s:
            c, r = s.pop()
            if (c, r) not in visited:
                visited.add((c, r))
                image[r][c] = color
                for dir in directions:
                    neighbour_c = c+dir[0]
                    neighbour_r = r+dir[1]
                    if self._within_bounds(image, neighbour_r, neighbour_c) and image[neighbour_r][neighbour_c] == starting_color:
                        s.append((neighbour_c, neighbour_r))
        return image

    def print_image(self, image):
        for row in image:
            print(row)
        print()

if __name__ == "__main__":
    solution = Solution()
    image = [[1,1,1],
             [1,1,0],
             [1,0,1]]
    sr = 1
    sc = 1
    color = 2
    # solution.print_image(solution.flood_fill_bfs(image, sr, sc, color))
    # solution.print_image(solution.flood_fill_dfs(image, sr, sc, color))
    solution.print_image(solution.flood_fill_dfs_iterative(image, sr, sc, color))
