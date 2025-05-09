import numpy as np
from typing import Tuple, Optional

class NeuralNetworks:
    class CNN:
        """
        Simple implementation of Convolutional Neural Network components.
        """
        @staticmethod
        def conv2d(input_data: np.ndarray, kernel: np.ndarray, 
                   stride: int = 1, padding: int = 0) -> np.ndarray:
            """
            2D convolution operation.
            
            Args:
                input_data: Input data of shape (batch_size, height, width, channels)
                kernel: Convolution kernel of shape (kernel_height, kernel_width, in_channels, out_channels)
                stride: Stride for convolution
                padding: Zero padding size
                
            Returns:
                Output feature map
            """
            # Get dimensions
            batch_size, in_height, in_width, in_channels = input_data.shape
            kernel_height, kernel_width, _, out_channels = kernel.shape
            
            # Calculate output dimensions
            out_height = (in_height + 2 * padding - kernel_height) // stride + 1
            out_width = (in_width + 2 * padding - kernel_width) // stride + 1
            
            # Initialize output
            output = np.zeros((batch_size, out_height, out_width, out_channels))
            
            # Pad input if needed
            if padding > 0:
                padded_input = np.pad(
                    input_data,
                    ((0, 0), (padding, padding), (padding, padding), (0, 0)),
                    mode='constant'
                )
            else:
                padded_input = input_data
            
            # Perform convolution
            for b in range(batch_size):
                for h in range(out_height):
                    for w in range(out_width):
                        for c_out in range(out_channels):
                            # Calculate input region
                            h_start = h * stride
                            h_end = h_start + kernel_height
                            w_start = w * stride
                            w_end = w_start + kernel_width
                            
                            # Extract input region
                            input_region = padded_input[b, h_start:h_end, w_start:w_end, :]
                            
                            # Apply kernel
                            output[b, h, w, c_out] = np.sum(input_region * kernel[:, :, :, c_out])
            
            return output
        
        @staticmethod
        def max_pool2d(input_data: np.ndarray, pool_size: int = 2, 
                       stride: Optional[int] = None) -> np.ndarray:
            """
            2D max pooling operation.
            
            Args:
                input_data: Input data of shape (batch_size, height, width, channels)
                pool_size: Size of pooling window
                stride: Stride for pooling (defaults to pool_size if None)
                
            Returns:
                Pooled feature map
            """
            # Get dimensions
            batch_size, in_height, in_width, channels = input_data.shape
            
            # Default stride to pool_size if not specified
            if stride is None:
                stride = pool_size
            
            # Calculate output dimensions
            out_height = (in_height - pool_size) // stride + 1
            out_width = (in_width - pool_size) // stride + 1
            
            # Initialize output
            output = np.zeros((batch_size, out_height, out_width, channels))
            
            # Perform max pooling
            for b in range(batch_size):
                for h in range(out_height):
                    for w in range(out_width):
                        for c in range(channels):
                            # Calculate input region
                            h_start = h * stride
                            h_end = h_start + pool_size
                            w_start = w * stride
                            w_end = w_start + pool_size
                            
                            # Extract input region
                            input_region = input_data[b, h_start:h_end, w_start:w_end, c]
                            
                            # Apply max pooling
                            output[b, h, w, c] = np.max(input_region)
            
            return output
        
        @staticmethod
        def relu(x: np.ndarray) -> np.ndarray:
            """ReLU activation function."""
            return np.maximum(0, x)
        
        @staticmethod
        def softmax(x: np.ndarray) -> np.ndarray:
            """Softmax activation function."""
            # Shift for numerical stability
            shifted_x = x - np.max(x, axis=-1, keepdims=True)
            exp_x = np.exp(shifted_x)
            return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    class Transformer:
        """
        Simple implementation of Transformer components.
        """
        @staticmethod
        def scaled_dot_product_attention(q: np.ndarray, k: np.ndarray, v: np.ndarray, 
                                         mask: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
            """
            Scaled dot-product attention mechanism.
            
            Args:
                q: Query tensor of shape (..., seq_len_q, depth)
                k: Key tensor of shape (..., seq_len_k, depth)
                v: Value tensor of shape (..., seq_len_v, depth_v)
                mask: Optional mask tensor
                
            Returns:
                Tuple of (attention_output, attention_weights)
            """
            # Calculate attention scores
            matmul_qk = np.matmul(q, k.transpose(0, 2, 1))
            
            # Scale attention scores
            depth = k.shape[-1]
            scaled_attention_logits = matmul_qk / np.sqrt(depth)
            
            # Apply mask if provided
            if mask is not None:
                scaled_attention_logits += (mask * -1e9)
            
            # Apply softmax to get attention weights
            attention_weights = NeuralNetworks.Transformer.softmax(scaled_attention_logits)
            
            # Apply attention weights to values
            output = np.matmul(attention_weights, v)
            
            return output, attention_weights
        
        @staticmethod
        def softmax(x: np.ndarray) -> np.ndarray:
            """Softmax function with numerical stability."""
            # Shift for numerical stability
            shifted_x = x - np.max(x, axis=-1, keepdims=True)
            exp_x = np.exp(shifted_x)
            return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
        
        @staticmethod
        def positional_encoding(position: int, d_model: int) -> np.ndarray:
            """
            Generate positional encoding for transformer models.
            
            Args:
                position: Maximum sequence length
                d_model: Embedding dimension
                
            Returns:
                Positional encoding matrix of shape (1, position, d_model)
            """
            # Initialize encoding matrix
            pos_encoding = np.zeros((position, d_model))
            
            # Calculate positional encodings
            for pos in range(position):
                for i in range(0, d_model, 2):
                    angle = pos / np.power(10000, (2 * i) / d_model)
                    pos_encoding[pos, i] = np.sin(angle)
                    if i + 1 < d_model:
                        pos_encoding[pos, i + 1] = np.cos(angle)
            
            # Add batch dimension
            pos_encoding = pos_encoding[np.newaxis, ...]
            
            return pos_encoding
        
        @staticmethod
        def feed_forward_network(x: np.ndarray, d_model: int, dff: int) -> np.ndarray:
            """
            Position-wise feed-forward network for transformer models.
            
            Args:
                x: Input tensor
                d_model: Model dimension
                dff: Hidden layer dimension
                
            Returns:
                Output tensor
            """
            # Random weights for demonstration (in practice, these would be learned)
            w1 = np.random.randn(d_model, dff) * 0.01
            b1 = np.zeros(dff)
            w2 = np.random.randn(dff, d_model) * 0.01
            b2 = np.zeros(d_model)
            
            # First dense layer with ReLU
            hidden = np.matmul(x, w1) + b1
            hidden = np.maximum(0, hidden)  # ReLU
            
            # Second dense layer
            output = np.matmul(hidden, w2) + b2
            
            return output
