# AlgoKit: A Comprehensive Algorithm Library

AlgoKit is a Python-based algorithm library that implements a wide range of algorithms in a modular, reusable way. This library is structured to allow easy integration into other projects.

## Features

AlgoKit provides implementations of the following algorithm categories:

### Sorting Algorithms
- Bubble Sort
- Quick Sort
- Merge Sort
- Heap Sort

### Graph Algorithms
- Dijkstra's Shortest Path

### Link Analysis Algorithms
- PageRank
- HITS (Hyperlink-Induced Topic Search)

### Cryptography Algorithms
- RSA Encryption/Decryption
- Integer Factorization (Trial Division and Pollard's Rho)
- Secure Hash Algorithms (SHA-256, SHA-512)

### Compression Algorithms
- Huffman Coding

### Neural Network Algorithms
- CNN Components (Convolution, Pooling, Activation Functions)
- Transformer Components (Attention Mechanism, Positional Encoding)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shaifulshabuj/algokit.git
cd algokit
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Here's a simple example of how to use AlgoKit:

```python
from algokit import Sorting, Graph, Cryptography

# Sort an array
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = Sorting.quick_sort(arr)
print(sorted_arr)  # [1, 2, 5, 5, 6, 9]

# Create a graph and find shortest paths
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
# ... add more edges
distances = g.dijkstra(0)
print(distances)  # Distances from vertex 0 to all other vertices

# RSA encryption/decryption
public_key, private_key = Cryptography.RSA.generate_keypair()
encrypted = Cryptography.RSA.encrypt(42, public_key)
decrypted = Cryptography.RSA.decrypt(encrypted, private_key)
print(decrypted)  # 42
```

For more detailed examples, see the `example.py` file.

## Key Design Principles

- **Modularity**: Each algorithm is encapsulated in its own class or method, making it easy to use independently.
- **Type Annotations**: The code uses Python type hints to improve readability and enable static type checking.
- **Documentation**: Comprehensive docstrings explain the purpose, parameters, and return values of each function.
- **Performance Considerations**: Implementations balance readability with efficiency.

## Requirements

- Python 3.7+
- NumPy

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
