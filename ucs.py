"""
Uniform Cost Search (UCS) Implementation
Nama: Divanda Firdaus
NIM: 32602500023
"""

import heapq
from graph_data import get_weighted_graph_data, get_test_nodes

class WeightedGraph:
    def __init__(self):
        self.graph = get_weighted_graph_data()
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
    
    def ucs(self, start, goal):
        """
        UCS implementation using priority queue
        Returns (path, total_cost) from start to goal if found, None otherwise
        """
        # Priority queue: (cumulative_cost, node, path)
        pq = [(0, start, [start])]
        visited = set()
        
        while pq:
            (cost, node, path) = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == goal:
                return (path, cost)
            
            if node in self.graph:
                for neighbor, edge_cost in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + edge_cost
                        heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
        
        return None
    
    def get_all_paths_cost(self, start, goal):
        """
        Alternative implementation to find all paths with their costs
        Returns list of (path, cost) tuples
        """
        paths = []
        
        def dfs(current, goal, path, cost, visited):
            if current == goal:
                paths.append((path.copy(), cost))
                return
            
            if current in visited:
                return
            
            visited.add(current)
            
            if current in self.graph:
                for neighbor, edge_cost in self.graph[current]:
                    if neighbor not in visited:
                        path.append(neighbor)
                        dfs(neighbor, goal, path, cost + edge_cost, visited)
                        path.pop()
            
            visited.remove(current)
        
        dfs(start, goal, [start], 0, set())
        return sorted(paths, key=lambda x: x[1])  # Sort by cost


# Example usage and test
if __name__ == "__main__":
    # Create weighted graph using centralized data
    wg = WeightedGraph()
    
    # Get test nodes from centralized data
    start_node, goal_node = get_test_nodes()
    
    print("Uniform Cost Search (UCS) Algorithm Test")
    print("=" * 50)
    print(f"Start Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print(f"Weighted Graph Data: {wg.graph}")
    print()
    
    print("Uniform Cost Search:")
    result = wg.ucs(start_node, goal_node)
    
    if result:
        path, total_cost = result
        print(f"Optimal path from {start_node} to {goal_node}: {path}")
        print(f"Total cost: {total_cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
    
    # Show all possible paths with costs for comparison
    print("\nAll possible paths (sorted by cost):")
    all_paths = wg.get_all_paths_cost(start_node, goal_node)
    for i, (path, cost) in enumerate(all_paths, 1):
        print(f"Path {i}: {path} - Cost: {cost}")