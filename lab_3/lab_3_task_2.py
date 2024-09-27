
import heapq
from collections import defaultdict


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

    # Додавання вузла
    def insert(self, key):
        self._insert_recursive(self.root, key)

    # Рекурсивне додавання нового елемента
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Прямий обхід дерева (in-order traversal)
    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            return self._inorder_recursive(node.left) + [node.key] + self._inorder_recursive(node.right)
        else:
            return []

    # Пошук елемента в дереві
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)




class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Перевизначення порівняння вузлів за частотою
    def __lt__(self, other):
        return self.freq < other.freq

# Побудова дерева Хаффмана
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Створення нового вузла, що об'єднує два найменших
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]

# Генерація кодів Хаффмана
def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root:
        # Якщо це листок
        if root.char is not None:
            codes[root.char] = current_code

        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Основна функція кодування Хаффмана
def huffman_encoding(data):
    # Підрахунок частот символів
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1

    # Побудова дерева Хаффмана
    huffman_tree = build_huffman_tree(frequencies)

    # Генерація кодів
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Кодування даних
    encoded_data = ''.join([huffman_codes[char] for char in data])

    return encoded_data, huffman_tree

# Основна функція декодування Хаффмана
def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = []
    node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        # Якщо це листок
        if node.left is None and node.right is None:
            decoded_data.append(node.char)
            node = huffman_tree

    return ''.join(decoded_data)

# Приклад використання
if __name__ == "__main__":
    data = "hello huffman"
    print(f"Original data: {data}")

    encoded_data, huffman_tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f"Decoded data: {decoded_data}")
