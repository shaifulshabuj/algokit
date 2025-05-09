from typing import List
import heapq

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u: int, v: int, w: int = 1):
        """Add edge to graph with optional weight."""
        self.graph[u].append((v, w))
    
    def dijkstra(self, src: int) -> List[int]:
        """
        Implementation of Dijkstra's algorithm for finding shortest paths.
        Time Complexity: O((V+E)logV) with binary heap
        Space Complexity: O(V)
        
        Returns list of distances from source to all vertices.
        """
        # Initialize distances as infinity for all vertices except source
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        # Priority queue to store vertices that need to be processed
        pq = [(0, src)]  # (distance, vertex)
        
        # Set to keep track of vertices included in shortest path tree
        visited = set()
        
        while pq:
            # Get vertex with minimum distance
            d, u = heapq.heappop(pq)
            
            # If already processed, skip
            if u in visited:
                continue
            
            # Mark as processed
            visited.add(u)
            
            # Update distances to adjacent vertices
            for v, weight in self.graph[u]:
                if v not in visited and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist
