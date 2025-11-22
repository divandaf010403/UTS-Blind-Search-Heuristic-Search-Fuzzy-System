"""
A* (A-Star) Search Implementation
Nama: Divanda Firdaus
NIM: 32602500023
"""

import heapq
import math
from graph_data import get_weighted_graph_data, get_heuristics_data, get_test_nodes, get_grid_data

class AStarGraph:
    def __init__(self):
        self.graph = get_weighted_graph_data()
        self.heuristics = get_heuristics_data()
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
    
    def set_heuristic(self, node, value):
        """Set heuristic value for a node"""
        self.heuristics[node] = value
    
    def set_heuristics(self, heuristic_dict):
        """Set heuristic values for multiple nodes"""
        self.heuristics.update(heuristic_dict)
    
    def calculate_euclidean_distance(self, node1_pos, node2_pos):
        """Calculate Euclidean distance between two points"""
        x1, y1 = node1_pos
        x2, y2 = node2_pos
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calculate_manhattan_distance(self, node1_pos, node2_pos):
        """Calculate Manhattan distance between two points"""
        x1, y1 = node1_pos
        x2, y2 = node2_pos
        return abs(x2 - x1) + abs(y2 - y1)
    
    def astar(self, start, goal):
        """
        A* implementation using priority queue
        Returns (path, total_cost) from start to goal if found, None otherwise
        """
        # Priority queue: (f_cost, g_cost, node, path)
        # f_cost = g_cost + h_cost
        pq = [(self.heuristics.get(start, 0), 0, start, [start])]
        visited = set()
        
        while pq:
            (f_cost, g_cost, node, path) = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == goal:
                return (path, g_cost)
            
            if node in self.graph:
                for neighbor, edge_cost in self.graph[node]:
                    if neighbor not in visited:
                        new_g_cost = g_cost + edge_cost
                        h_cost = self.heuristics.get(neighbor, 0)
                        f_cost = new_g_cost + h_cost
                        heapq.heappush(pq, (f_cost, new_g_cost, neighbor, path + [neighbor]))
        
        return None
    
    def reconstruct_path(self, came_from, current):
        """Helper method to reconstruct path from came_from dictionary"""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]  # Reverse to get from start to goal


# Example usage and test
if __name__ == "__main__":
    # Create A* graph using centralized data
    astar_graph = AStarGraph()
    
    # Get test nodes from centralized data
    start_node, goal_node = get_test_nodes()
    
    print("A* Search Algorithm Test")
    print("=" * 50)
    print(f"Start Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print(f"Weighted Graph Data: {astar_graph.graph}")
    print(f"Heuristics Data: {astar_graph.heuristics}")
    print()
    
    print("A* Search:")
    result = astar_graph.astar(start_node, goal_node)
    
    if result:
        path, total_cost = result
        print(f"Optimal path from {start_node} to {goal_node}: {path}")
        print(f"Total cost: {total_cost}")
        
        # Show step-by-step breakdown
        print("\nPath breakdown:")
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            edge_cost = None
            for neighbor, cost in astar_graph.graph[current]:
                if neighbor == next_node:
                    edge_cost = cost
                    break
            print(f"{current} -> {next_node}: cost = {edge_cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
    
    # Example with grid-based heuristic using centralized data
    print("\n--- Grid-based A* Example ---")
    grid_graph = AStarGraph()
    
    # Get grid data from centralized source
    positions, connections = get_grid_data()
    
    # Create grid connections (4-directional movement)
    for node, neighbors in connections.items():
        for neighbor in neighbors:
            grid_graph.add_edge(node, neighbor, 1)
    
    # Set Manhattan distance heuristics
    goal_pos = positions['Goal']
    for node_name, node_pos in positions.items():
        h = grid_graph.calculate_manhattan_distance(node_pos, goal_pos)
        grid_graph.set_heuristic(node_name, h)
    
    result = grid_graph.astar('Start', 'Goal')
    if result:
        path, cost = result
        print(f"Grid path: {path}")
        print(f"Total cost: {cost}")