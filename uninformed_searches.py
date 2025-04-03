def dfs(graph, start, goal, getPathOnly=0):
    visited = []
    unvisited = []
    paths = {start: [start]}
    expanded_nodes = 0
    if start == goal:
        return ("Path taken: " + str(paths[start]) + "\nTotal nodes expanded: 0")
    unvisited.append(start)
    start_node = ""
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
    visited = []
    unvisited = []
    paths = {start: [start]}
    expanded_nodes = 0
    if start == goal:
        return ("Path taken: " + str(paths[start]) + "\nTotal nodes expanded: 0")
    unvisited.append(start)
    start_node = ""
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
        return "goal not in graph"
    


def ucs(graph, start, goal):
    visited = []
    unvisited = [(0, start)]
    paths = {start: [start]}
    best_cost = {start: 0}
    expanded_nodes = 0
    if start == goal:
        return ("Path taken: "+ str(paths[start]) + "\nTotal nodes expanded: 0" )
    start_node = ""

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


def printGraph(graph):
    print("Graph Visualization:")
    for node, neighbors in graph.items():
        neighbor_str = ", ".join([f"{node} -> {neighbor}(cost={cost})" for neighbor, cost in neighbors])
        print(f"{neighbor_str}") 



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
    print("DFS UCS and BFS algorithm demo done by Kibreab")
    printGraph(graph)
    try:
        while True:
            print("Interactive demo of DFS and BFS search algorithms\n")
            print("input exit or ctrl-C to exit the demo")

            sNode = input("enter a starting node from the above graph or type exit: ").upper()
            gNode = input("enter a goal node from the above graph or type exit: ").upper()

            if sNode == "EXIT" or gNode == "EXIT":
                break
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
    except KeyboardInterrupt:
        print("\nProgram exiting...")

