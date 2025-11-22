"""
Centralized Graph Data for Search Algorithms
Nama: Divanda Firdaus
NIM: 32602500023

File ini berisi data graf yang dapat digunakan oleh semua algoritma search
(DFS, UCS, A*) untuk konsistensi data dan kemudahan pemeliharaan.
"""

# Data graf untuk algoritma tanpa bobot (DFS)
GRAPH_DATA = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['I'],
    'G': ['I'],
    'H': [],
    'I': []
}

# Data graf berbobot untuk UCS dan A*
WEIGHTED_GRAPH_DATA = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 2)],
    'C': [('D', 8), ('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': [('I', 2)],
    'H': [('I', 6)],
    'I': []
}

# Data heuristik untuk A* (estimasi jarak ke tujuan)
HEURISTICS_DATA = {
    'A': 8,
    'B': 6,
    'C': 7,
    'D': 2,
    'E': 4,
    'F': 2,
    'G': 2,
    'H': 6,
    'I': 0  # Tujuan memiliki heuristik 0
}

# Node start dan goal untuk testing
START_NODE = 'A'
GOAL_NODE = 'I'

# Data grid untuk contoh A* grid-based
GRID_POSITIONS = {
    'Start': (0, 0),
    'A': (0, 1),
    'B': (0, 2),
    'C': (1, 0),
    'D': (1, 1),
    'E': (1, 2),
    'F': (2, 0),
    'G': (2, 1),
    'Goal': (2, 2)
}

# Koneksi grid (4-directional movement)
GRID_CONNECTIONS = {
    'Start': ['A', 'C'],
    'A': ['Start', 'B', 'D'],
    'B': ['A', 'E'],
    'C': ['Start', 'D', 'F'],
    'D': ['A', 'C', 'E', 'G'],
    'E': ['B', 'D', 'Goal'],
    'F': ['C', 'G'],
    'G': ['D', 'F', 'Goal'],
    'Goal': ['E', 'G']
}

def get_graph_data():
    """Mengembalikan data graf untuk DFS"""
    return GRAPH_DATA

def get_weighted_graph_data():
    """Mengembalikan data graf berbobot untuk UCS dan A*"""
    return WEIGHTED_GRAPH_DATA

def get_heuristics_data():
    """Mengembalikan data heuristik untuk A*"""
    return HEURISTICS_DATA

def get_grid_data():
    """Mengembalikan data grid untuk contoh A* grid-based"""
    return GRID_POSITIONS, GRID_CONNECTIONS

def get_test_nodes():
    """Mengembalikan node start dan goal untuk testing"""
    return START_NODE, GOAL_NODE

def print_graph_info():
    """Menampilkan informasi graf untuk debugging"""
    print("=== GRAPH DATA INFORMATION ===")
    print(f"Start Node: {START_NODE}")
    print(f"Goal Node: {GOAL_NODE}")
    
    print("\nUnweighted Graph (for DFS):")
    for node, neighbors in GRAPH_DATA.items():
        print(f"  {node}: {neighbors}")
    
    print("\nWeighted Graph (for UCS, A*):")
    for node, edges in WEIGHTED_GRAPH_DATA.items():
        print(f"  {node}: {edges}")
    
    print("\nHeuristics (for A*):")
    for node, h_value in HEURISTICS_DATA.items():
        print(f"  {node}: {h_value}")

if __name__ == "__main__":
    print_graph_info()