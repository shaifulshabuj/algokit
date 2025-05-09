import heapq

class Compression:
    class HuffmanCoding:
        class Node:
            def __init__(self, char, freq):
                self.char = char
                self.freq = freq
                self.left = None
                self.right = None
            
            def __lt__(self, other):
                return self.freq < other.freq
        
        def __init__(self):
            self.heap = []
            self.codes = {}
            self.reverse_mapping = {}
        
        def _make_frequency_dict(self, text):
            """Create frequency dictionary for input text."""
            frequency = {}
            for char in text:
                if char not in frequency:
                    frequency[char] = 0
                frequency[char] += 1
            return frequency
        
        def _make_heap(self, frequency):
            """Create a priority queue from frequency dictionary."""
            for key in frequency:
                node = self.Node(key, frequency[key])
                heapq.heappush(self.heap, node)
        
        def _merge_nodes(self):
            """Merge nodes until only one remains (the root)."""
            while len(self.heap) > 1:
                node1 = heapq.heappop(self.heap)
                node2 = heapq.heappop(self.heap)
                
                merged = self.Node(None, node1.freq + node2.freq)
                merged.left = node1
                merged.right = node2
                
                heapq.heappush(self.heap, merged)
        
        def _make_codes_helper(self, node, current_code):
            """Recursively generate codes for each character."""
            if node is None:
                return
            
            if node.char is not None:
                self.codes[node.char] = current_code
                self.reverse_mapping[current_code] = node.char
            
            self._make_codes_helper(node.left, current_code + "0")
            self._make_codes_helper(node.right, current_code + "1")
        
        def _make_codes(self):
            """Generate Huffman codes."""
            root = heapq.heappop(self.heap)
            current_code = ""
            self._make_codes_helper(root, current_code)
            # Put the root back for decoding
            heapq.heappush(self.heap, root)
        
        def _get_encoded_text(self, text):
            """Encode text using Huffman codes."""
            encoded_text = ""
            for char in text:
                encoded_text += self.codes[char]
            return encoded_text
        
        def _pad_encoded_text(self, encoded_text):
            """Pad encoded text to make its length a multiple of 8."""
            padding = 8 - (len(encoded_text) % 8)
            if padding == 8:
                padding = 0
            
            # Add padding information at the beginning
            padded_info = format(padding, '08b')
            padded_text = padded_info + encoded_text
            
            # Add padding
            for _ in range(padding):
                padded_text += "0"
            
            return padded_text
        
        def _bytes_from_bits(self, padded_text):
            """Convert bit string to bytes."""
            b = bytearray()
            for i in range(0, len(padded_text), 8):
                byte = padded_text[i:i+8]
                b.append(int(byte, 2))
            return bytes(b)
        
        def compress(self, text):
            """
            Compress text using Huffman coding.
            
            Args:
                text: Input text to compress
                
            Returns:
                Tuple of (compressed_data, huffman_tree)
            """
            # Reset state
            self.heap = []
            self.codes = {}
            self.reverse_mapping = {}
            
            # Build Huffman tree
            frequency = self._make_frequency_dict(text)
            self._make_heap(frequency)
            self._merge_nodes()
            self._make_codes()
            
            # Encode text
            encoded_text = self._get_encoded_text(text)
            padded_text = self._pad_encoded_text(encoded_text)
            compressed_data = self._bytes_from_bits(padded_text)
            
            # Return compressed data and the Huffman tree (for decompression)
            return compressed_data, self.heap[0]
        
        def _remove_padding(self, bit_string):
            """Remove padding from bit string."""
            padded_info = bit_string[:8]
            padding = int(padded_info, 2)
            
            # Remove padding information and padding
            bit_string = bit_string[8:]
            if padding > 0:
                bit_string = bit_string[:-padding]
            
            return bit_string
        
        def _bits_from_bytes(self, data):
            """Convert bytes to bit string."""
            bit_string = ""
            for byte in data:
                # Convert byte to 8-bit binary string
                binary = format(byte, '08b')
                bit_string += binary
            return bit_string
        
        def _decode_text(self, encoded_text, root):
            """Decode text using Huffman tree."""
            current = root
            decoded_text = ""
            
            for bit in encoded_text:
                if bit == '0':
                    current = current.left
                else:
                    current = current.right
                
                if current.char is not None:
                    decoded_text += current.char
                    current = root
            
            return decoded_text
        
        def decompress(self, compressed_data, huffman_tree):
            """
            Decompress data using Huffman coding.
            
            Args:
                compressed_data: Compressed data
                huffman_tree: Huffman tree root node
                
            Returns:
                Decompressed text
            """
            bit_string = self._bits_from_bytes(compressed_data)
            encoded_text = self._remove_padding(bit_string)
            decompressed_text = self._decode_text(encoded_text, huffman_tree)
            
            return decompressed_text
