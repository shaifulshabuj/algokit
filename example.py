#!/usr/bin/env python3
"""
AlgoKit Example Script
This script demonstrates how to use the various algorithms in the AlgoKit library.
"""

from algokit import Sorting, Graph, LinkAnalysis, Cryptography, Compression, NeuralNetworks
import numpy as np

def sorting_examples():
    """Demonstrate sorting algorithms."""
    print("\n===== SORTING ALGORITHMS =====")
    arr = [5, 2, 9, 1, 5, 6]
    print("Original array:", arr)
    print("Bubble sort:", Sorting.bubble_sort(arr))
    print("Quick sort:", Sorting.quick_sort(arr))
    print("Merge sort:", Sorting.merge_sort(arr))
    print("Heap sort:", Sorting.heap_sort(arr))

def graph_examples():
    """Demonstrate graph algorithms."""
    print("\n===== GRAPH ALGORITHMS =====")
    # Create a graph with 9 vertices
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    
    print("Dijkstra's shortest paths from vertex 0:")
    distances = g.dijkstra(0)
    for i, dist in enumerate(distances):
        print(f"Vertex {i}: {dist}")

def link_analysis_examples():
    """Demonstrate link analysis algorithms."""
    print("\n===== LINK ANALYSIS ALGORITHMS =====")
    # Create a simple web graph
    web_graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1, 4],
        4: [1, 2, 3]
    }
    
    print("PageRank:")
    pr = LinkAnalysis.pagerank(web_graph, iterations=20)
    for node, score in pr.items():
        print(f"Node {node}: {score:.6f}")
    
    print("\nHITS Algorithm:")
    hub_scores, auth_scores = LinkAnalysis.hits(web_graph, iterations=20)
    print("Hub scores:")
    for node, score in hub_scores.items():
        print(f"Node {node}: {score:.6f}")
    print("Authority scores:")
    for node, score in auth_scores.items():
        print(f"Node {node}: {score:.6f}")

def cryptography_examples():
    """Demonstrate cryptography algorithms."""
    print("\n===== CRYPTOGRAPHY ALGORITHMS =====")
    # RSA encryption/decryption
    print("RSA Encryption/Decryption:")
    # Use small key size for demonstration purposes
    public_key, private_key = Cryptography.RSA.generate_keypair(bits=64)
    message = 42
    encrypted = Cryptography.RSA.encrypt(message, public_key)
    decrypted = Cryptography.RSA.decrypt(encrypted, private_key)
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")
    
    # Integer factorization
    n = 1001
    print(f"\nFactors of {n} (trial division): {Cryptography.integer_factorization(n, 'trial_division')}")
    print(f"Factors of {n} (Pollard's rho): {Cryptography.integer_factorization(n, 'pollard_rho')}")
    
    # Hash functions
    text = "Hello, AlgoKit!"
    print(f"\nSHA-256 of '{text}': {Cryptography.sha256(text)}")
    print(f"SHA-512 of '{text}': {Cryptography.sha512(text)}")

def compression_examples():
    """Demonstrate compression algorithms."""
    print("\n===== COMPRESSION ALGORITHMS =====")
    # Huffman coding
    text = "this is an example for huffman encoding"
    huffman = Compression.HuffmanCoding()
    compressed, tree = huffman.compress(text)
    decompressed = huffman.decompress(compressed, tree)
    
    print(f"Original text: {text}")
    print(f"Compressed size: {len(compressed)} bytes")
    print(f"Original size: {len(text)} bytes")
    print(f"Compression ratio: {len(compressed) / len(text):.2f}")
    print(f"Decompressed text: {decompressed}")

def neural_network_examples():
    """Demonstrate neural network algorithms."""
    print("\n===== NEURAL NETWORK ALGORITHMS =====")
    # CNN example
    print("CNN Example:")
    # Create random input and kernel
    input_data = np.random.randn(1, 5, 5, 3)  # 1 image, 5x5, 3 channels
    kernel = np.random.randn(3, 3, 3, 2)  # 3x3 kernel, 3 input channels, 2 output channels
    
    # Apply convolution
    conv_output = NeuralNetworks.CNN.conv2d(input_data, kernel, stride=1, padding=1)
    print(f"Input shape: {input_data.shape}")
    print(f"Kernel shape: {kernel.shape}")
    print(f"Convolution output shape: {conv_output.shape}")
    
    # Apply max pooling
    pool_output = NeuralNetworks.CNN.max_pool2d(conv_output, pool_size=2, stride=2)
    print(f"Max pooling output shape: {pool_output.shape}")
    
    # Transformer example
    print("\nTransformer Example:")
    # Create random query, key, value tensors
    batch_size = 1
    seq_len = 4
    d_model = 8
    
    q = np.random.randn(batch_size, seq_len, d_model)
    k = np.random.randn(batch_size, seq_len, d_model)
    v = np.random.randn(batch_size, seq_len, d_model)
    
    # Apply attention
    attention_output, attention_weights = NeuralNetworks.Transformer.scaled_dot_product_attention(q, k, v)
    print(f"Attention output shape: {attention_output.shape}")
    print(f"Attention weights shape: {attention_weights.shape}")
    
    # Generate positional encoding
    pos_encoding = NeuralNetworks.Transformer.positional_encoding(seq_len, d_model)
    print(f"Positional encoding shape: {pos_encoding.shape}")

if __name__ == "__main__":
    print("AlgoKit: A Comprehensive Algorithm Library")
    print("=========================================")
    
    sorting_examples()
    graph_examples()
    link_analysis_examples()
    cryptography_examples()
    compression_examples()
    neural_network_examples()
    
    print("\nAll examples completed successfully!")
