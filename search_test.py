import time
import uninformed_searches


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
        print(f"\n--- Test: {test_name} ---")

        # Measure BFS time
        start_time = time.time()
        bfs_result = uninformed_searches.bfs(unweighted_graph, start, goal)
        bfs_time = time.time() - start_time
        print(f"BFS {start} to {goal}: {bfs_result} (Time: {bfs_time:.6f} seconds)")

        # Measure DFS time
        start_time = time.time()
        dfs_result = uninformed_searches.dfs(unweighted_graph, start, goal)
        dfs_time = time.time() - start_time
        print(f"DFS {start} to {goal}: {dfs_result} (Time: {dfs_time:.6f} seconds)")

        # Measure UCS time
        start_time = time.time()
        ucs_result = uninformed_searches.ucs(graph, start, goal)
        ucs_time = time.time() - start_time
        print(f"UCS {start} to {goal}: {ucs_result} (Time: {ucs_time:.6f} seconds)")

        # Measure IDDFS time
        start_time = time.time()
        iddfs_result = uninformed_searches.iddfs(graph, start, goal, 10)
        iddfs_time = time.time() - start_time
        print(f"IDDFS {start} to {goal}: {iddfs_result} (Time: {iddfs_time:.6f} seconds)")

if __name__ == "__main__":
    run_tests()
