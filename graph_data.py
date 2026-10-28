 # Pre-defined city graph with edge weights (distances)
 # Expanded City Graph with nodes from A to M
city_graph = {
    'A': {'B': 4, 'C': 2, 'F': 5},
    'B': {'A': 4, 'C': 1, 'D': 5, 'G': 7},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10, 'H': 3},
    'D': {'B': 5, 'C': 8, 'E': 2, 'I': 4},
    'E': {'C': 10, 'D': 2, 'J': 6},
    'F': {'A': 5, 'G': 2, 'K': 8},
    'G': {'B': 7, 'F': 2, 'H': 3, 'L': 4},
    'H': {'C': 3, 'G': 3, 'I': 5, 'M': 6},
    'I': {'D': 4, 'H': 5, 'J': 3},
    'J': {'E': 6, 'I': 3, 'M': 2},
    'K': {'F': 8, 'L': 3},
    'L': {'G': 4, 'K': 3, 'M': 5},
    'M': {'H': 6, 'J': 2, 'L': 5}
}
