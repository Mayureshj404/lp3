import heapq
from collections import defaultdict

def huffman_encoding(data):
    # Frequency dictionary
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Priority queue (min-heap)
    heap = [[freq, [char, ""]] for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Generate codes
    huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return {char: code for char, code in huffman_codes}

def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code, decoded_data = "", ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ""

    return decoded_data

# Example usage
data = "hello huffman"
huffman_codes = huffman_encoding(data)
encoded_data = ''.join(huffman_codes[char] for char in data)
print(f"Encoded Data: {encoded_data}")
print(f"Huffman Codes: {huffman_codes}")

decoded_data = huffman_decoding(encoded_data, huffman_codes)
print(f"Decoded Data: {decoded_data}")