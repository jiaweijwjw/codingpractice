import enum

image = [[1,1,1],
        [1,1,0],
        [1,0,1]]
sr = 1
sc = 1
color = 2

class Dir(enum.Enum):
    up = 0, -1
    right = 1, 0
    down = 0, 1
    left = -1, 0

def solution(image, sr, sc, color):
    visited = set()
    dfs_fill(image, (sc, sr), color, image[sr][sc], visited) # becareful again, row is y, col is x
    return image

def dfs_fill(image, coord, color, original_color, visited):
    visited.add(coord)
    image[coord[1]][coord[0]] = color
    for dir in Dir:
        neighbour = tuple(sum(i) for i in zip(coord, dir.value))
        if 0 <= neighbour[0] < len(image[0]) and 0 <= neighbour[1] < len(image) and neighbour not in visited and image[neighbour[1]][neighbour[0]] == original_color:
            dfs_fill(image, neighbour, color, original_color, visited)

print(image)
print()
print(solution(image, sr, sc, color))