from collections import deque
from uninformed_searches import bfs

def translate_maze_to_graph(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    graph = {}  # Create a graph representation of the maze

    def get_neighbors(row, col):
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors

    # Create the graph from the maze
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 0:
                graph[(r, c)] = get_neighbors(r, c)

    path = bfs(graph, start, end,1)
    return path

# Example Maze
maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
to_edit = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

print("Initial maze")
for j in maze:
    print (j)


path = translate_maze_to_graph(maze, start, end)

for x, y in path:
    if (x, y )== start:
        to_edit[x][y] = "s"
    elif (x,y) == end:
        to_edit[x][y] = "g"
    else:
        to_edit[x][y] = "*"

if path:
    print("===============Solution==============")
    for i in to_edit:
        print (i)
else:
    print("Maze BFS: No path found.")
