from typing import Dict, List, Tuple
import numpy as np

class LinkAnalysis:
    @staticmethod
    def pagerank(graph: Dict[int, List[int]], damping: float = 0.85, iterations: int = 100, 
                 tolerance: float = 1e-6) -> Dict[int, float]:
        """
        Implementation of the PageRank algorithm.
        Time Complexity: O(k * (V + E)) where k is the number of iterations
        Space Complexity: O(V)
        
        Args:
            graph: Dictionary mapping node IDs to lists of outgoing links
            damping: Damping factor (typically 0.85)
            iterations: Maximum number of iterations
            tolerance: Convergence threshold
            
        Returns:
            Dictionary mapping node IDs to PageRank scores
        """
        nodes = list(graph.keys())
        n = len(nodes)
        
        # Initialize PageRank scores
        pr = {node: 1/n for node in nodes}
        
        # Create a mapping from node ID to index
        node_to_idx = {node: i for i, node in enumerate(nodes)}
        
        # Precompute outgoing link counts
        outgoing_counts = {node: len(outlinks) for node, outlinks in graph.items()}
        
        # Iteratively update PageRank scores
        for _ in range(iterations):
            next_pr = {node: (1 - damping) / n for node in nodes}
            
            # Update based on incoming links
            for node, outlinks in graph.items():
                if outgoing_counts[node] > 0:  # Avoid division by zero
                    for outlink in outlinks:
                        if outlink in next_pr:  # Ensure the outlink is in our graph
                            next_pr[outlink] += damping * pr[node] / outgoing_counts[node]
            
            # Check for convergence
            diff = sum(abs(next_pr[node] - pr[node]) for node in nodes)
            pr = next_pr
            
            if diff < tolerance:
                break
        
        return pr
    
    @staticmethod
    def hits(graph: Dict[int, List[int]], iterations: int = 100, 
             tolerance: float = 1e-6) -> Tuple[Dict[int, float], Dict[int, float]]:
        """
        Implementation of the HITS (Hyperlink-Induced Topic Search) algorithm.
        Time Complexity: O(k * (V + E)) where k is the number of iterations
        Space Complexity: O(V)
        
        Args:
            graph: Dictionary mapping node IDs to lists of outgoing links
            iterations: Maximum number of iterations
            tolerance: Convergence threshold
            
        Returns:
            Tuple of (hub_scores, authority_scores) dictionaries
        """
        nodes = list(graph.keys())
        
        # Create reverse graph (incoming links)
        reverse_graph = {node: [] for node in nodes}
        for node, outlinks in graph.items():
            for outlink in outlinks:
                if outlink in reverse_graph:
                    reverse_graph[outlink].append(node)
        
        # Initialize hub and authority scores
        hub_scores = {node: 1.0 for node in nodes}
        auth_scores = {node: 1.0 for node in nodes}
        
        for _ in range(iterations):
            # Update authority scores
            new_auth = {node: 0.0 for node in nodes}
            for node in nodes:
                for inlink in reverse_graph[node]:
                    new_auth[node] += hub_scores[inlink]
            
            # Normalize authority scores
            auth_sum = sum(score**2 for score in new_auth.values()) ** 0.5
            if auth_sum > 0:
                for node in nodes:
                    new_auth[node] /= auth_sum
            
            # Update hub scores
            new_hub = {node: 0.0 for node in nodes}
            for node in nodes:
                for outlink in graph[node]:
                    if outlink in new_auth:  # Ensure the outlink is in our graph
                        new_hub[node] += new_auth[outlink]
            
            # Normalize hub scores
            hub_sum = sum(score**2 for score in new_hub.values()) ** 0.5
            if hub_sum > 0:
                for node in nodes:
                    new_hub[node] /= hub_sum
            
            # Check for convergence
            auth_diff = sum(abs(new_auth[node] - auth_scores[node]) for node in nodes)
            hub_diff = sum(abs(new_hub[node] - hub_scores[node]) for node in nodes)
            
            auth_scores = new_auth
            hub_scores = new_hub
            
            if auth_diff < tolerance and hub_diff < tolerance:
                break
        
        return hub_scores, auth_scores
