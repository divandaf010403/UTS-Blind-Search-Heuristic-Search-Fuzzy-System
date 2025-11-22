"""
Depth-First Search (DFS) Implementation
Nama: Divanda Firdaus
NIM: 32602500023
"""

from collections import deque
from graph_data import get_graph_data, get_test_nodes

class Graph:
    def __init__(self):
        self.graph = get_graph_data()
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs(self, start, goal):
        """
        DFS implementation using stack
        Returns path from start to goal if found, None otherwise
        """
        visited = set()
        stack = [(start, [start])]
        
        while stack:
            (node, path) = stack.pop()
            
            if node not in visited:
                visited.add(node)
                
                if node == goal:
                    return path
                
                # Add neighbors to stack (reverse order for consistent results)
                if node in self.graph:
                    for neighbor in reversed(self.graph[node]):
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor]))
        
        return None
    
    def dfs_recursive(self, start, goal, visited=None, path=None):
        """
        Recursive DFS implementation
        """
        if visited is None:
            visited = set()
        if path is None:
            path = [start]
        
        visited.add(start)
        
        if start == goal:
            return path
        
        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    result = self.dfs_recursive(neighbor, goal, visited, path + [neighbor])
                    if result is not None:
                        return result
        
        return None


# Example usage and test
if __name__ == "__main__":
    # Create graph using centralized data
    g = Graph()
    
    # Get test nodes from centralized data
    start_node, goal_node = get_test_nodes()
    
    print("DFS Algorithm Test")
    print("=" * 50)
    print(f"Start Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print(f"Graph Data: {g.graph}")
    print()
    
    print("DFS Iterative:")
    path = g.dfs(start_node, goal_node)
    print(f"Path from {start_node} to {goal_node}: {path}")
    
    print("\nDFS Recursive:")
    path_recursive = g.dfs_recursive(start_node, goal_node)
    print(f"Path from {start_node} to {goal_node}: {path_recursive}")