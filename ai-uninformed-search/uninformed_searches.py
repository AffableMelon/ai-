import time

def dfs(graph, start, goal, getPathOnly=0):
    visited = [] # visited list of nodes to not visit again
    unvisited = [] # our fringe as a LIFO stack
    paths = {start: [start]} # all found paths for each node 
    expanded_nodes = 0 # keep tracks of how many nodes we've visited so far
    if start == goal: # base case
        return ("Path taken: " + str(paths[start]) + "\nTotal nodes expanded: 0")
    unvisited.append(start)
    start_node = ""
    '''
    while our fringe has a state
    pop the very last entry (last in first out)
    check if its the goal state
    return if it is
    check the children of the current states and put them inside our fringe if they haven't been visited
    mark the parent state as visited 
    repeate till you find the goal.
    '''
    while unvisited:
        start_node = unvisited.pop()
        expanded_nodes+=1 
        visited.append(start_node)
        if start_node == goal:
            break
        for node in graph[start_node]:
            if node not in visited:
                unvisited.append(node)
                paths[node] = paths[start_node] + [node]

    if start_node == goal:
        if getPathOnly:
            return(paths[goal])
        return ("Path taken: " + str(paths[goal]) + "\nTotal nodes expanded: " + str(expanded_nodes))
    else:
        return "goal not in graph"



def bfs(graph, start, goal, getPathOnly=0):
    visited = [] # visited list of nodes to not visit again
    unvisited = [] # our fringe as a FIFO queue
    paths = {start: [start]} # all found paths for each node
    expanded_nodes = 0 # keep tracks of how many nodes we've visited so far
    if start == goal: # base case
        return ("Path taken: " + str(paths[start]) + "\nTotal nodes expanded: 0")
    unvisited.append(start)
    start_node = ""
    '''
    while our fringe has a state
    pop the very first entry (first in first out)
    check if its the goal state
    return if it is
    check the children of the current states and put them inside our fringe if they haven't been visited or are already in the fringe.
    mark the parent state as visited
    repeat till you find the goal.
    '''
    while unvisited:
        start_node = unvisited.pop(0)
        visited.append(start_node)
        expanded_nodes+=1 
        if start_node == goal:
            break
        for node in graph[start_node]:
            if node not in visited and node not in unvisited:
                unvisited.append(node)
                paths[node] = paths[start_node] + [node]

    if start_node == goal:
        if getPathOnly:
            return(paths[goal])
        return ("Path taken: " + str(paths[goal]) + "\nTotal nodes expanded: " + str(expanded_nodes))
    else:
        if getPathOnly:
            return(False)
        return "goal not in graph"
    


def ucs(graph, start, goal):
    visited = [] # List of visited nodes
    unvisited = [(0, start)] # Priority queue (cost, node)
    paths = {start: [start]}  # Dictionary to store paths to each node
    best_cost = {start: 0} # Dictionary to store the best cost to each node
    expanded_nodes = 0 # Counter for expanded nodes
    if start == goal: # Base case: start and goal are the same
        return ("Path taken: "+ str(paths[start]) + "\nTotal nodes expanded: 0" )
    start_node = ""
    '''
    while our fringe has a state
    sort the fringe based on cost
    pop the very first entry (lowest cost)
    check if its the goal state
    return if it is
    check the children of the current states and put them inside our fringe if they haven't been visited or have a lower cost.
    mark the parent state as visited
    repeat till you find the goal.
    '''
    while unvisited: 
        unvisited.sort()
        cost, start_node = unvisited.pop(0)
        visited.append(start_node)
        expanded_nodes+=1 
        if start_node == goal:
            break
        for node, edge_cost in graph[start_node]:
            new_cost = cost + edge_cost
            if node not in best_cost or new_cost < best_cost[node]:
                best_cost[node] = new_cost
                paths[node] = paths[start_node] + [node]
                unvisited.append((new_cost, node))

    if (start_node == goal):
        return ("Path taken: "+ str(paths[start_node]) + "\nTotal nodes expanded: "+ str(expanded_nodes))
    else: 
        return("goal not in graph")

def dfs_limited(graph, start, goal, depth_limit):
    """DFS with a depth limit."""
    visited = []
    unvisited = [(start, [start])]  # Stack with path
    expanded_nodes = 0

    while unvisited:
        node, path = unvisited.pop()
        expanded_nodes += 1
        if node == goal:
            return path, expanded_nodes
        if len(path) <= depth_limit and node not in visited:
            visited.append(node)
            for neighbor, cost in graph[node]:
                unvisited.append((neighbor, path + [neighbor]))
    return None, expanded_nodes  # Depth limit reached or goal not found

def iddfs(graph, start, goal, max_depth=10):
    """Iterative Deepening DFS."""
    for depth in range(max_depth + 1):  # Iterate through depth limits
        result, expanded_nodes = dfs_limited(graph, start, goal, depth)
        if result:
            return result, expanded_nodes
    return None, 0  # Goal not found within max_depth

# ========= Helper functions ========

def printGraph(graph):
    print("Graph Visualization:")
    for node, neighbors in graph.items():
        neighbor_str = ", ".join([f"{node} -> {neighbor}(cost={cost})" for neighbor, cost in neighbors])
        print(f"{neighbor_str}") 


def run_tests():
    test_cases = [
        ('A', 'F', "A to F"),
        ('C', 'D', "C to D"),
        ('H', 'B', "H to B"),
        ('A', 'H', "A to H"),
        ('B', 'G', "B to G"),
        ('I', 'A', "I to A"),
        ('A', 'I', "A to I"),
        ('A', 'A', "A to A"),
        ('C', 'G', "C to G")
    ]

    for start, goal, test_name in test_cases:
        print(f"\n--- Test: {test_name} --- ")

        # BFS Performance
        start_time = time.perf_counter()
        bfs_result = bfs(unweighted_graph, start, goal)
        end_time = time.perf_counter()
        bfs_time = end_time - start_time
        print(f"BFS {start} to {goal}: {bfs_result} (Time: {bfs_time:.6f} seconds)")

        # DFS Performance
        start_time = time.perf_counter()
        dfs_result = dfs(unweighted_graph, start, goal)
        end_time = time.perf_counter()
        dfs_time = end_time - start_time
        print(f"DFS {start} to {goal}: {dfs_result} (Time: {dfs_time:.6f} seconds)")

        # UCS Performance
        start_time = time.perf_counter()
        ucs_result = ucs(graph, start, goal)
        end_time = time.perf_counter()
        ucs_time = end_time - start_time
        print(f"UCS {start} to {goal}: {ucs_result} (Time: {ucs_time:.6f} seconds)")

        # IDDFS Performance
        start_time = time.perf_counter()
        iddfs_result = iddfs(graph, start, goal, 10)
        end_time = time.perf_counter()
        iddfs_time = end_time - start_time
        print(f"IDDFS {start} to {goal}: {iddfs_result} (Time: {iddfs_time:.6f} seconds)")


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

def printMaze(maze):
    for j in maze:
        for k in j:
            print(k, end=' ')
        print("\n")


def run_maze(maze, start, end):
    print("Initial maze")
    printMaze(maze)
    print("Start is:" + str(start) + "\nEnd is: " + str(end))
    path = translate_maze_to_graph(maze, start, end)
    if path:
        for x, y in path:
            if (x, y )== start:
                maze[x][y] = "s"
            elif (x,y) == end:
                maze[x][y] = "g"
            else:
                maze[x][y] =  "█"
        print("===============Solution==============")
        printMaze(maze)
    else:
        print("Maze BFS: No path found.")

# =============== variables used ===================
maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (3, 4)

graph = {
   'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 1)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 3), ('G', 2)],
    'E': [('B', 1), ('F', 1), ('H', 4)],
    'F': [('C', 5), ('E', 1)],
    'G': [('D', 2)],
    'H': [('E', 4)],
    'I': []
}

unweighted_graph = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'F'], 
    'D': ['B', 'G'], 
    'E': ['B', 'F', 'H'], 
    'F': ['C', 'E'], 
    'G': ['D'], 
    'H': ['E'], 
    'I': []
}


if __name__ == '__main__':
    print("Uninformed Search algorithms demo done by Kibreab")
    try:
        while True:
            print("<------------------------------------------------------------------->\n")
            print("This demo has 3 parts\n1 interactive demo of all four algorithims\n2 unit test for each algorithm \n3 maze search with bfs algorithm\n4 path finding with cost involved UCS\n")
            print("input exit or ctrl-C to exit the demo at any time")
            choice = int(input("Please enter a value 1-4 to pick which youd like to see: "))
            if (choice == 1):
                printGraph(graph)
                sNode = input("Enter a starting node from the above graph: ").upper()
                gNode = input("Enter a goal node from the above graph: ").upper()

                print("The DFS solution is: ", end ='')
                print(dfs(unweighted_graph, sNode, gNode))
                print("<==============================>")
                print("The BFS solution is: ", end = '')
                print(bfs(unweighted_graph, sNode, gNode))
                print("<==============================>")
                print("The UCS solution is: ", end = '')
                print(ucs(graph, sNode, gNode))
                print("<==============================>")
                print("The IDDFS solution is: ", end = '')
                print(iddfs(graph, sNode, gNode))
            elif (choice == 2):   
                run_tests()
            elif (choice == 3):
                run_maze(maze,start,end)
            elif (choice == 4):
                printGraph(graph)
                print("A good example here is a path from A to F or from F to A\nThere are two paths one with a cost of nine and a cost of 4\nOther paths can be used too just an example\n")
                sNode = input("Enter a starting node from the above graph: ").upper()
                gNode = input("Enter a goal node from the above graph: ").upper()
                print(ucs(graph, sNode, gNode))
            else: 
                print("Sorry that input isnt supported try again\n")
    except KeyboardInterrupt:
        print("\nProgram exiting...")

